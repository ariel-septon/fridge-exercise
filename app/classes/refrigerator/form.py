from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired
from ...models import Shelf


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
    shelves_list = QuerySelectMultipleField(query_factory=lambda: Shelf.query.all(),
                                            get_label="level_number")
    submit = SubmitField('Create')
    """def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')"""
