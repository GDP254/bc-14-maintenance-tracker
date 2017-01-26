#import db
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Facility(db.Model):
	__tablename__ = 'facilities'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	status = db.Column(db.String(64), unique=False)
	requests = db.relationship('Request', backref='facility', lazy='dynamic')

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
	requests = db.relationship('Request', backref='user', lazy='dynamic')

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

class Request(db.Model):
	__tablename__ = 'request'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=False)
	photo = db.Column(db.String(64), unique=False, nullable=True)
	notes = db.Column(db.String(200), unique=False)
	status = db.Column(db.String(64), unique=False, default='default')
	facility_id = db.Column(db.Integer, db.ForeignKey('facilities.id'))#db.ForeignKey('facilities.id')
	admin_comment = db.Column(db.String(200), unique=False)
	assignee_name = db.Column(db.String(64), unique=False)
	assignee_number = db.Column(db.String(64), unique=False)
	assignment_date = db.Column(db.String(64), unique=False)
	assignment_time = db.Column(db.String(64), unique=False)
	#user_id = db.Column(db.Integer, unique=False)
	admin_id = db.Column(db.Integer, unique=False)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	#admin_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	user_requests = db.relationship('User', foreign_keys=[user_id], backref='user')
	#admin_requests = db.relationship('User', foreign_keys=[admin_id], backref='admin')

	def __repr__(self):
		return '<Request %r>' % self.name

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))