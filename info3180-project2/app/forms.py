from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField,validators,PasswordField


class ContactForm(FlaskForm):
  uname=StringField('Name',[validators.DataRequired()])
  password = PasswordField('New Password', [ validators.DataRequired()])
  fname=StringField('First Name',[validators.DataRequired()])
  lname=StringField('Last Name'),[validators.DataRequired()])    
  email=StringField('Email Address',[validators.DataRequired()])
  location=StringField('Location',[validators.DataRequired()])
  biography =TextAreaField('Biography',[validators.Length(min=20, max=40)])

