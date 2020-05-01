from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField, RadioField
from wtforms.validators import DataRequired
from ...models import Item, Shelf
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField


class CreateAnItemForm(FlaskForm):
    """
    Form for users to create new item
    """
    name = StringField('Name', validators=[DataRequired()])
    type_category = SelectField('Type category', validators=[DataRequired()], choices=[('food', 'food'),
                                                                                       ('drink', 'drink')])
    kosher_category = SelectField('Kosher category', validators=[DataRequired()], choices=[('dairy', 'dairy'),
                                                                                           ('parve', 'parve'),
                                                                                           ('meat', 'meat')])
    expiration_date = DateField('Expiration date', validators=[DataRequired()])
    place_taken = IntegerField('Place taken', validators=[DataRequired()])
    submit = SubmitField('Submit')
    """def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')"""
