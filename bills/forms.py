from django.forms import ModelForm
from django import forms

from bills.models import Bill


class CreateBillForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    type = forms.ChoiceField(choices=Bill.TYPE_CHOICES)
    amount = forms.DecimalField()
    file = forms.FileField()

