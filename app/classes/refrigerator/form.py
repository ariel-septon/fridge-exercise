from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateARefrigeratorForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])

    submit = SubmitField('Create')