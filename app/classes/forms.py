from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
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


class ChooseRefrigerator1(FlaskForm):
    refrigerator1 = QuerySelectField(query_factory=lambda: Refrigerator.query.all(),
                                             get_label="model")
    type_category = SelectField('Type category', validators=[DataRequired()], choices=[('food', 'food'),
                                                                                       ('drink', 'drink')])
    kosher_category = SelectField('Kosher category', validators=[DataRequired()], choices=[('dairy', 'dairy'),
                                                                                           ('parve', 'parve'),
                                                                                           ('meat', 'meat')])
    submit = SubmitField('Choose')


class ChooseRefrigerator2(FlaskForm):
    refrigerator2 = QuerySelectField(query_factory=lambda: Refrigerator.query.all(),
                                             get_label="model")
    submit = SubmitField('Choose')


class AddAnItemToRefrigerator(FlaskForm):
    refrigerator = QuerySelectField(query_factory=lambda: Refrigerator.query.all(),
                                             get_label="model")
    item = QuerySelectField(query_factory=lambda: Item.query.all(),
                                             get_label="name")
    submit = SubmitField('Choose')


class RemoveItemFromRefrigerator(FlaskForm):
    refrigerator__ = QuerySelectField(query_factory=lambda: Refrigerator.query.all(),
                                             get_label="model")
    item__ = QuerySelectField(query_factory=lambda: Item.query.all(),
                                             get_label="name")
    submit = SubmitField('Choose')
