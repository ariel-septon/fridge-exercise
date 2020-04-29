from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from ...models import Item


class CreateAnItemForm(FlaskForm):
    """
    Form for users to create new item
    """
    name = StringField('Name', validators=[DataRequired()])
    shelf_located = IntegerField('Shelf located', validators=[DataRequired()])
    type_category = StringField('Type category', validators=[DataRequired()])
    kosher_category = StringField('Kosher category', validators=[DataRequired()])
    expiration_date = StringField('Expiration date', validators=[DataRequired()])
    place_taken = IntegerField('Place taken', validators=[DataRequired()])
    submit = SubmitField('Submit')
    """def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')"""
