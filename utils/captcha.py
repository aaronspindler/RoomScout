from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms


class Captcha(forms.Form):
	captcha = ReCaptchaField(widget=ReCaptchaV3, label='')
