from django.forms import *


class LoginForm(Form):
	username = CharField(label='Username')
	password = CharField(widget=PasswordInput())
