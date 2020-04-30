from app import db


class Item(db.Model):
    """
    Create a Item table
    """

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    # shelf_located = db.Column(db.Integer)
    type_category = db.Column(db.String(60))
    kosher_category = db.Column(db.String(60))
    expiration_date = db.Column(db.DATE)
    place_taken = db.Column(db.Integer)
    # foreign key
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelves.id'))

    def __repr__(self):
        return '<Item: {}>'.format(self.name)


class Shelf(db.Model):
    """
    Create a shelf table
    """

    __tablename__ = 'shelves'

    id = db.Column(db.Integer, primary_key=True)
    level_number = db.Column(db.Integer)
    place_size = db.Column(db.Integer)
    items_list = db.relationship('Item', backref='shelf',
                                 lazy='dynamic')
    # foreign key
    refrigerator_id = db.Column(db.Integer, db.ForeignKey('refrigerators.id'))

    def __repr__(self):
        return '<Shelf: {}>'.format(self.name)


class Refrigerator(db.Model):
    """
    Create a refrigerator table
    """

    __tablename__ = 'refrigerators'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(60), unique=True)
    color = db.Column(db.String(60))
    shelves_list = db.relationship('Shelf',
                                   backref='refrigerator',
                                   lazy='dynamic')

    def __repr__(self):
        return '<Refrigerator: {}>'.format(self.name)
