from flask import Flask, render_template, url_for, flash, redirect
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from forms import EmailForm
from models import User

import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is just a test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'email.sqlite')
#boilerplate for config for database

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
	email_form = EmailForm()
	if email_form.validate_on_submit():
		email_address = email_form.email.data
		prev_user = User.query.filter_by(email = email_address).first()
		if (prev_user is not None):
			if (prev_user.verified):
				flash('That email address has already been submitted and verified')
			else:
				#the situation where a previous email has already been seen
				flash('That email address is already in our records but we will resend the verification email.')
				return redirect(url_for('index'))

			#NEED TO HANDLE CASE WHERE EMAIL ALREADY EXISTS
		new_user = User(email=email_address, date_submitted=datetime.now())
		db.session.add(new_user)
		db.session.commit()
		token = user.generate_confirmation_token()
		send_verification_email('email/confirm', 'Confirm Your Account', user=user, token = token)
 
		return redirect(url_for('thanks'))

	return render_template('index.html', form = email_form)


@app.route('/thanks')
def thanks():
	return render_template('thanks.html')


@app.route('/confirm/<token>')
def confirm(token):
	if 


def send_verfication_email():
	pass


if __name__ == '__main__':
	app.run(debug=True)