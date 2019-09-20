from django import forms
from captcha.fields import ReCaptchaField

from captcha.widgets import ReCaptchaV3

class Captcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')