from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from ...models import Shelf


class CreateAShelfForm(FlaskForm):
    """
    Form for users to create new shelf
    self.id = id_number_generator()
        self.level_number = level_number
        self.place_size = place_size
        self.items_list = items_list
        self.place_left = place_size - sum(item.place_taken for item in self.items_list)
    """
    level_number = StringField('Level number', validators=[DataRequired()])
    place_size = StringField('Place  size', validators=[DataRequired()])
    submit = SubmitField('Create')
    """def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')"""
