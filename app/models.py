from app import db


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
    items_list = db.relationship('Item', backref='shelf',
                                 lazy='dynamic')

    place_left = db.Column(db.Integer)

    # foreign key
    refrigerator_id = db.Column(db.Integer, db.ForeignKey('refrigerators.id'))

    def __repr__(self):
        return '<Shelf: {}>'.format(self.name)

    def __init__(self):
        self.place_left = self.place_size - sum(item.place_taken for item in self.items_list)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Shelf):
            return False
        """
        return other.level_number == self.level_number and \
               other.place_size == self.place_size and \
               other.place_left == self.place_left and \
               other.items_list == self.items_list
        """
        return other.level_number == self.level_number and \
               other.place_size == self.place_size and \
               other.place_left == self.place_left


class Refrigerator(db.Model):
    __tablename__ = 'refrigerators'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(60), unique=True)
    color = db.Column(db.String(60))
    shelves_list = db.relationship('Shelf',
                                   backref='refrigerator',
                                   lazy='dynamic')

    shelf_amount = db.Column(db.Integer)

    def __repr__(self):
        return '<Refrigerator: {}>'.format(self.name)

    def __init__(self):
        self.shelf_amount = len(self.shelves_list)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Refrigerator):
            return False
        """
        return other.model == self.model and \
               other.color == self.color and \
               other.shelf_amount == self.shelf_amount and \
               other.shelves_list == self.shelves_list
        """
        return other.model == self.model and \
               other.color == self.color and \
               other.shelf_amount == self.shelf_amount
