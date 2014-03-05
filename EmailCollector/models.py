from flask.ext.sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), unique = True)
	verified = db.Column(db.Boolean, default = False)
	date_submitted = db.Column(db.DateTime)
	date_verified = db.Column(db.DateTime)

	def generate_confirmation_token(self, expiration=3600): #expiration in seconds
		s = Serializer(app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm': self.id})

	def confirm(self, token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except:
			return False

		if data.get('confirm') != self.id:
			return False

		self.verified = True
		db.session.add(self)
		db.session.commit()
		return True

