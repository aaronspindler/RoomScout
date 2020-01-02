from django.forms import ModelForm
from django import forms

from bills.models import Bill


class CreateBillForm(ModelForm):
    file = forms.FileField()
    class Meta:
        model = Bill
        fields = ['date', 'type', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker', 'id': 'date'})
        }
