from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['address', 'city', 'prov_state', 'postal_code', 'country']
        labels = {'prov_state':'Province/State'}
