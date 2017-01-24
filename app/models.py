#import db
from app import db

class Facility(db.Model):
	__tablename__ = 'facilities'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	status = db.Column(db.String(6), unique=False)

	def __repr__(self):
		return '<Facility %r>' % self.name