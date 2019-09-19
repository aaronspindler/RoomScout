from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class AllauthSignupForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible, label='')
    field_order = ['email','password1','password2','captcha']

    def signup(self, request, user):
        """ Required, or else it throws deprecation warnings """
        pass

class PreferencesForm(forms.Form):
    bill_contact = forms.BooleanField(label='Yes, I would like RoomScout to contact me about new bills in Houses that I am a member of.', required=False)
    promo_contact = forms.BooleanField(label='Yes, I would like RoomScout to contact me about events, new features, and other promotional information.', required=False)

class VerificationForm(forms.Form):
    phone_number = forms.CharField(max_length=20, label='Phone Number', required=False)