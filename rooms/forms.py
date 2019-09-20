from django import forms


class FilterForm(forms.Form):
	max_price = forms.IntegerField(label='Max Price:', required=False)
	pets_allowed = forms.BooleanField(label='Pets Allowed', required=False)
	#num_rooms = forms.IntegerField(label='Number of Rooms:', required=False)
	#num_bathrooms = forms.IntegerField(label='Number of Bathrooms:', required=False)
	#num_parking_spaces = forms.IntegerField(label='Number of Parking spaces:', required=False)
	#has_dishwasher = forms.BooleanField(label='Has Dishwasher', required=False)
	#has_laundry = forms.BooleanField(label='Has On-site Laundry', required=False)
	#has_air_conditioning = forms.BooleanField(label='Has Air Conditioning', required=False)
