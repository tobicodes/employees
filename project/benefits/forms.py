from flask_wtf import FlaskForm, Form
from wtforms import TextField, IntegerField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Benefit


class NewBenefitForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])
    cost_per_employee =IntegerField('Cost',validators=[DataRequired()])