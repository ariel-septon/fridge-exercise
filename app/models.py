from app import db
from app.helpers.utils import is_expired
from app.helpers.utils import is_item_fits_categories
from app.helpers.utils import remove_items_due_specific_expiration_date_and_kosher_category
from app.helpers.utils import insert_the_fresh_items_back_to_fridge


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    type_category = db.Column(db.String(60))
    kosher_category = db.Column(db.String(60))
    expiration_date = db.Column(db.DATE)
    place_taken = db.Column(db.Integer)
    # foreign key
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelves.id'))

    def __repr__(self):
        return '<Item: {}>'.format(self.name)

    def __init__(self, name: str, shelf_located: int, type_category: str, kosher_category: str,
                 expiration_date, place_taken):
        self.name = name
        self.shelf_located = shelf_located
        self.type_category = type_category
        self.kosher_category = kosher_category
        self.expiration_date = expiration_date
        self.place_taken = place_taken

    def __eq__(self, other) -> bool:
        if not isinstance(other, Item):
            return False
        return other.name == self.name and \
               other.type_category == self.type_category and \
               other.kosher_category == self.kosher_category and \
               other.expiration_date == self.expiration_date and \
               other.place_taken == self.place_taken


class Shelf(db.Model):
    __tablename__ = 'shelves'

    id = db.Column(db.Integer, primary_key=True)
    level_number = db.Column(db.Integer)
    place_size = db.Column(db.Integer)
    place_left = db.Column(db.Integer)
    items_list = db.relationship('Item', backref='shelf')

    # foreign key
    refrigerator_id = db.Column(db.Integer, db.ForeignKey('refrigerators.id'))

    def __repr__(self):
        return '<Shelf: {}>'.format(self.name)

    def __init__(self, level_number: int, place_size: int):
        self.level_number = level_number
        self.place_size = place_size
        self.place_left = place_size
        self.items_list = []

    def __eq__(self, other) -> bool:
        if not isinstance(other, Shelf):
            return False
        return other.level_number == self.level_number and \
               other.place_size == self.place_size and \
               other.place_left == self.place_left and \
               other.items_list == self.items_list


class Refrigerator(db.Model):
    __tablename__ = 'refrigerators'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(60), unique=True)
    color = db.Column(db.String(60))
    shelf_amount = db.Column(db.Integer)
    shelves_list = db.relationship('Shelf',
                                   backref='refrigerators')

    def __repr__(self):
        return '<Refrigerator: {}>'.format(self.name)

    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        self.shelves_list = []
        self.shelf_amount = 0

    def __eq__(self, other) -> bool:
        if not isinstance(other, Refrigerator):
            return False
        return other.model == self.model and \
               other.color == self.color and \
               other.shelf_amount == self.shelf_amount and \
               other.shelves_list == self.shelves_list

    def place_left_in_the_fridge(self) -> int:
        return sum(shelf.place_left for shelf in self.shelves_list)

    def add_a_shelf(self, shelf: Shelf):
        self.shelves_list.append(shelf)
        db.session.add(self)
        db.session.commit()

    def add_an_item(self, item: Item) -> bool:
        for shelf in self.shelves_list:
            if shelf.place_size >= item.place_taken:
                shelf.items_list.append(item)
                item.shelf_located = shelf.level_number
                shelf.place_left = shelf.place_size - item.place_taken
                db.session.add(self)
                db.session.commit()
                return True
        return False

    def take_out_an_item(self, id_number) -> Item:
        for shelf in self.shelves_list:
            item = next((item for item in shelf.items_list if item.id == id_number), None)
            if item is not None:
                shelf.items_list.remove(item)
                shelf.place_left = shelf.place_left + item.place_taken
                db.session.add(self)
                db.session.commit()
                return item
        raise ValueError('The item is not currently in the refrigerator')

    def cleanup(self) -> None:
        for shelf in self.shelves_list:
            for item in shelf.items_list:
                if is_expired(item):
                    self.take_out_an_item(item.id)
        db.session.add(self)
        db.session.commit()

    def whats_to_eat(self, kosher_category, type_category) -> list:
        foods_list = []
        for shelf in self.shelves_list:
            foods_list.extend([item for item in shelf.items_list if
                               is_item_fits_categories(item, kosher_category, type_category)])
        return foods_list

    def getting_shopping_ready(self) -> None:
        kosher_category_and_days_before_expiration = {
            'dairy': 3, 'meat': 7, 'parve': 1,
        }
        first_cleanup = True
        save_items = {}
        for kosher, days in kosher_category_and_days_before_expiration.items():
            if self.place_left_in_the_fridge() < 20 and first_cleanup:
                self.cleanup()
                first_cleanup = False
                print('first cleanup ended')
            if self.place_left_in_the_fridge() < 20:
                print('if', kosher)
                remove_items_due_specific_expiration_date_and_kosher_category(self, days,
                                                                              kosher, save_items)
        if self.place_left_in_the_fridge() < 20:
            insert_the_fresh_items_back_to_fridge(self, save_items)
