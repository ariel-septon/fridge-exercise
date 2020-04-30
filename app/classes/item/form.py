from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateTimeField
from wtforms.validators import DataRequired
from ...models import Item, Shelf
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField


class CreateAnItemForm(FlaskForm):
    """
    Form for users to create new item
    """
    name = StringField('Name', validators=[DataRequired()])
    # shelf_located = QuerySelectField(query_factory=lambda: Shelf.query.all(),
    # get_label="level_number")
    type_category = SelectField('Type category', validators=[DataRequired()], choices=['food', 'drink'])
    kosher_category = SelectField('Kosher category', validators=[DataRequired()], choices=['dairy', 'parve', 'meat'])
    expiration_date = DateTimeField('Expiration date', validators=[DataRequired()])
    place_taken = IntegerField('Place taken', validators=[DataRequired()])
    submit = SubmitField('Submit')
    """def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')"""
