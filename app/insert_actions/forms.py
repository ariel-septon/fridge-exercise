from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
"""
from ..classes.item.Item import Item
from ..classes.shelf.shelf import Shelf"""
from ..models import Shelf, Item


class InsertAnItemToShelf(FlaskForm):
    item = QuerySelectField(query_factory=lambda: Item.query.all(),
                             get_label="name")
    submit = SubmitField('Submit')


class InsertAShelfToRefrigerator(FlaskForm):
    shelf = QuerySelectField(query_factory=lambda: Shelf.query.all(),
                                    get_label="level_number")
    submit = SubmitField('Submit')
