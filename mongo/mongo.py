from flask import Flask, render_template
#from flask.ext.pymongo import PyMongo
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

import os
import pymongo

basedir = os.path.abspath(os.path.dirname(__file__))


#still don't understand this yet, passing in dunder name dunder
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SECRET_KEY'] = 'this is secret'

db = SQLAlchemy(app)

#Database classes
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User', backref = 'role')

	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique = True, index = True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User %r>' % self.username


#Bootstrap
bootstrap = Bootstrap(app)

#MongoDB
'''
Flask-PyMongo threw unusual errors, we
will see if this causes problems later on.

app.config['MONGO_URI'] = 'mongodb://127.0.0.1'
#app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = 'test'
#app.config['MONGO_USERNAME'] = ''
#app.config['MONGO_PASSWORD'] = ''
mongo = PyMongo(app)
'''

host_string = "mongodb://localhost"
port = 27017
client = pymongo.MongoClient(host_string, port)

mongo_db = client['test']
tweets_collection = mongo_db['tweets_test']
usernames_collection = mongo_db['usernames_test']


#adding a route so it does something
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/settings')
def settings():
	return render_template('settings.html')


@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')


@app.route('/twitter/all_users')
def all_users():
	#this function will list all the users for a company
	return render_template('all_users.html')


@app.route('/twitter/user_profile/<screen_name>')
def user_profile(screen_name):
	user_profile = usernames_collection.find_one({'screen_name':screen_name})
	return render_template('user_profile.html', user_profile = user_profile, screen_name = screen_name)


@app.route('/twitter/tweets/<screen_name>')
def user_tweets(screen_name):
	tweets = tweets_collection.find({'user.id':16729151})

	#PyMongo returns a cursor which must be iterated over
	tweets_for_template = []
	for t in tweets:
		tweets_for_template.append(t)

	return render_template('tweets.html', tweets = tweets_for_template, screen_name = screen_name)


def init_db_with_data(db):
	db.drop_all()
	db.create_all()
	admin_role = Role(name='Admin')
	mod_role = Role(name='Moderator')
	user_role = Role(name='User')
	user_sean = User(username='murphsp1@gmail.com', role = admin_role)
	user_ben = User(username='ben', role = admin_role)

	db.session.add_all([admin_role, mod_role, user_role, user_sean, user_ben])
	db.session.commit()

#Only call this function once.
#init_db_with_data(db)



if __name__ == ('__main__'):
	app.run(debug=True)


