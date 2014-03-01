from flask import Flask, render_template
#from flask.ext.pymongo import PyMongo
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

import pymongo

#still don't understand this yet
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

#Bootstrap
bootstrap = Bootstrap(app)

#MongoDB
''' Flask-PyMongo threw unusual errors, we
will see what this means later on

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

db = client['test']
tweets_collection = db['tweets_test']
usernames_collection = db['usernames_test']


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



if __name__ == ('__main__'):
	app.run(debug=True)


