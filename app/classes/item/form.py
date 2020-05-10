from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired


class CreateAnItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    type_category = SelectField('Type category', validators=[DataRequired()], choices=[('food', 'food'),
                                                                                       ('drink', 'drink')])
    kosher_category = SelectField('Kosher category', validators=[DataRequired()], choices=[('dairy', 'dairy'),
                                                                                           ('parve', 'parve'),
                                                                                           ('meat', 'meat')])
    expiration_date = DateField('Expiration date', validators=[DataRequired()])
    place_taken = IntegerField('Place taken', validators=[DataRequired()])
    submit = SubmitField('Submit')