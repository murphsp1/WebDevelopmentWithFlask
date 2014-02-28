from flask import Flask, request, make_response, redirect, abort, render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)



#Routes for this test application

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent


@app.route('/response')
def response():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer','42')
	return response

@app.route('/redirect_test')
def redirect_test():
	return redirect('http://www.google.com/')


@app.route('/user/<name>')
def user(name):
	if not name:
		abort(404)
	return '<h1>Hello, %s!</h1>' % name



if __name__ == '__main__':
	#app.run(debug=True)
	manager.run()