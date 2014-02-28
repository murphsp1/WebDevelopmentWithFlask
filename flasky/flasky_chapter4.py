from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from datetime import datetime 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to get and guess string'
#this should really be stored as an environment variable

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
	name = StringField('What is your name?', validators = [Required()])
	submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session['name']
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		form.name.data=''
		return redirect(url_for('index'))
	return render_template('index.html',form = form, name = session.get('name'), current_time = datetime.utcnow())


if __name__ == '__main__':
	app.run(debug=True)

