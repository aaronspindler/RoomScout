from django import forms

from .models import House


class HouseForm(forms.ModelForm):
	class Meta:
		model = House
		fields = ['address', 'city', 'prov_state', 'postal_code', 'country', 'hide_address']
		labels = {'prov_state': 'Province/State'}
		help_texts = {'hide_address': "Use this if you don't want the exact address published!"}
