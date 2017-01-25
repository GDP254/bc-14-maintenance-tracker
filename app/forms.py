from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, ValidationError
from wtforms.validators import Required, length, Email, EqualTo
from models import User
from flask_login import current_user

class SigninForm(Form):
	email = StringField('Email:', validators=[Required()])
	password = PasswordField('Password:', validators=[Required()])
	remember = BooleanField('Remember me')
	signin = SubmitField('Sign In')

class RegisterForm(Form):
	fname = StringField('First Name:', validators=[Required(), length(1, 64)])
	lname = StringField('Last Name:', validators=[Required(), length(1, 64)])
	email = StringField('Email:', validators=[Required(), length(1, 64), Email()])
	password = PasswordField('Password:', 
					validators=[ 
					length(1, 120), 
					EqualTo('confirm_password', 
						message = 'Your passwords do not match.')])
	confirm_password = PasswordField('Confirm Password:', validators=[length(1, 120)])
	register = SubmitField('Register')

	def validate_email(self, field):
		if field.data != self.email and \
		User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

class UserForm(Form):
	fname = StringField('First Name:', validators=[Required(), length(1, 64)])
	lname = StringField('Last Name:', validators=[Required(), length(1, 64)])
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role:', choices=[('default', 'Default'), ('staff', 'Staff'), ('admin', 'Admin'), ('super-admin', 'Super-Admin')], validators=[Required()])
	submit = SubmitField('Submit')

class RegisterFacilityForm(Form):
	name = StringField('Name:', validators=[Required()])
	status = SelectField('Status:', choices=[('inactive', 'Inactive'), ('active', 'Active')], validators=[Required()])
	register = SubmitField('Register')