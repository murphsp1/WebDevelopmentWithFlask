from flask.ext.wtf import Form 
from wtforms import TextField, SubmitField
from wtforms.validators import Email, DataRequired

class EmailForm(Form):
	email = TextField('Email Address', validators = [DataRequired(), Email()])
	submit = SubmitField('Submit')