from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask import Markup

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    subject = StringField('Enter Subject', validators=[DataRequired()])
    body = TextAreaField('Enter Message Here', validators=[DataRequired()])
    submit = SubmitField('Submit')