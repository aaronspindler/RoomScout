from django import forms

from .models import Room


class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = ['name', 'price', 'is_available']
		labels = {}
		help_texts = {}
