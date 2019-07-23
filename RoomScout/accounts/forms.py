from django.forms import *
from .models import User

class LoginForm(Form):
    username = CharField(label='Username')
    password = CharField(widget=PasswordInput())
