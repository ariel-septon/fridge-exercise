from app.helpers.utils import id_number_generator
from app import db


class ShelfObj:
    def __init__(self, level_number, place_size, items_list):
        self.id = id_number_generator()
        self.level_number = level_number
        self.place_size = place_size
        self.items_list = items_list
        self.place_left = place_size - sum(item.place_taken for item in self.items_list)

"""
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
               other.items_list == self.items_list"""
