from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(Form):
	email = TextField('Email', validators = [Required(), Email()])
	username = TextField('Username', validators = [Required(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
				'Usernames must have only letters, numbers, dots, or underscores')])
	password = PasswordField('Password', validators = [
		Required(), EqualTo('password2', message = 'Passwords must match.')])
	password2 = PasswordField('Confirm password', validators = [Required()])
	submit = SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')

class LoginForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
