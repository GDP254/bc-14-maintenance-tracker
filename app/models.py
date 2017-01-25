#import db
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Facility(db.Model):
	__tablename__ = 'facilities'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	status = db.Column(db.String(6), unique=False)

	def __repr__(self):
		return '<Facility %r>' % self.name

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	fname = db.Column(db.String(64), unique=False)
	lname = db.Column(db.String(64), unique=False)
	email = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(120), unique=False)
	confirmed = db.Column(db.Boolean, default=False)
	role = db.Column(db.String(64), unique=False)
	#is_active = db.Column(db.Boolean, default=True)

	@property 
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
	"""
	def get_id(self):
		return self.id
	"""

	def __repr__(self):
		return '<User %r>' % self.fname

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))