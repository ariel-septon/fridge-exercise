from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Shelf, Item, Refrigerator


class CompareRefrigerators(FlaskForm):
    refrigerator1 = QuerySelectField(query_factory=lambda: Refrigerator.query.all(),
                                             get_label="model")
    refrigerator2 = QuerySelectField(query_factory=lambda: Refrigerator.query.all(),
                                             get_label="model")
    submit = SubmitField('Choose')


class CompareShelves(FlaskForm):
    shelf1 = QuerySelectField(query_factory=lambda: Shelf.query.all(),
                                             get_label="level_number")
    shelf2 = QuerySelectField(query_factory=lambda: Shelf.query.all(),
                                             get_label="level_number")
    submit = SubmitField('Choose')


class CompareItems(FlaskForm):
    item1 = QuerySelectField(query_factory=lambda: Item.query.all(),
                                             get_label="name")
    item2 = QuerySelectField(query_factory=lambda: Item.query.all(),
                                             get_label="name")
    submit = SubmitField('Choose')


class ChooseRefrigerator(FlaskForm):
    refrigerator = QuerySelectField(query_factory=lambda: Refrigerator.query.all(),
                                             get_label="model")
    submit = SubmitField('Choose')
