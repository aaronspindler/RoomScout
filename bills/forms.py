from django import forms
from django.forms import formset_factory

from bills.models import Bill


class BillForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'yyyy-mm-dd'}))
    type = forms.ChoiceField(choices=Bill.TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '100.00'}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))


BillFormset = formset_factory(BillForm, extra=4)