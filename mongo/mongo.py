from flask import Flask, render_template
#from flask.ext.pymongo import PyMongo
from flask.ext.bootstrap import Bootstrap
import pymongo


#still don't understand this yet
app = Flask(__name__)

#Bootstrap
bootstrap = Bootstrap(app)

#MongoDB
'''
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

@app.route('/user/<username>')
def user_profile(username):
	user = usernames_collection.find_one({'screen_name':username})
	return render_template('user.html', user = user)


if __name__ == ('__main__'):
	app.run(debug=True)