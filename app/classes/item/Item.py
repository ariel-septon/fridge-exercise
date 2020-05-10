from app.helpers.utils import id_number_generator
from app import db


class ItemObj:
    def __init__(self, name, shelf_located, type_category, kosher_category,
                 expiration_date, place_taken):
        self.id = id_number_generator()
        self.name = name
        self.shelf_located = shelf_located
        self.type_category = type_category
        self.kosher_category = kosher_category
        self.expiration_date = expiration_date
        self.place_taken = place_taken

"""
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
               other.place_taken == self.place_taken"""
