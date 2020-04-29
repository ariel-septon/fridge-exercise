from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from ...models import Refrigerator


class CreateARefrigeratorForm(FlaskForm):
    """
    Form for users to create new refrigerator
     self.id = id_number_generator()
        self.model = model
        self.color = color
        self.shelves_list = shelves_list
        self.shelf_amount = len(self.shelves_list)
    """
    model = StringField('Model', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    submit = SubmitField('Create')
    """def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')"""
