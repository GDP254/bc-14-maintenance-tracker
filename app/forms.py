from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required

class SigninForm(Form):
	email = StringField('Email:', validators=[Required()])
	password = PasswordField('Password:', validators=[Required()])
	remember = BooleanField('Remember me')
	signin = SubmitField('Sign In')

class RegisterForm(Form):
	fname = StringField('First Name:', validators=[Required()])
	lname = StringField('Last Name:', validators=[Required()])
	email = StringField('Email:', validators=[Required()])
	password = PasswordField('Password:', validators=[Required()])
	confirm_password = PasswordField('Confirm Password:', validators=[Required()])
	signin = SubmitField('Register')