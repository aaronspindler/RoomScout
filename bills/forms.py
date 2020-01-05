from django import forms

from bills.models import Bill


class CreateBillForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd'}))
    type = forms.ChoiceField(choices=Bill.TYPE_CHOICES)
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '100.00'}))
    file = forms.FileField()

