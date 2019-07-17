from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['address', 'country', 'prov_state', 'postal_code']
        labels = {'prov_state':'Province/State'}
