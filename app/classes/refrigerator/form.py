from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired
# from ...models import Shelf


class CreateARefrigeratorForm(FlaskForm):
    """
    Form for users to create new refrigerator
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
