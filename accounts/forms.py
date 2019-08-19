from django.forms import *
from captcha.fields import ReCaptchaField

class AllauthSignupForm(forms.Form):

    captcha = ReCaptchaField()
    field_order = ['email','password1','password2','captcha']

    def signup(self, request, user):
        """ Required, or else it throws deprecation warnings """
        pass