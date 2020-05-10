from app.helpers.utils import id_number_generator
from app.classes.shelf.shelf import ShelfObj
from app import db
from app.helpers.utils import is_expired
from app.helpers.utils import is_item_fits_categories
from app.helpers.utils import remove_items_due_specific_expiration_date_and_kosher_category
from app.helpers.utils import insert_the_fresh_items_back_to_fridge
# from ..shelf.shelf import Shelf
# from ..item.Item import Item

"""
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
"""


class RefrigeratorObj:
    def __init__(self, model, color, shelves_list: [ShelfObj]):
        self.id = id_number_generator()
        self.model = model
        self.color = color
        self.shelves_list = shelves_list
        self.shelf_amount = len(self.shelves_list)
