from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
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
	register = SubmitField('Register')

class RegisterFacilityForm(Form):
	name = StringField('Name:', validators=[Required()])
	status = SelectField('Status:', choices=[('Inactive', 'Inactive'), ('Active', 'Active')], validators=[Required()])
	register = SubmitField('Register')