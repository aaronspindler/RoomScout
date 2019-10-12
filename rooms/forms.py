from django import forms


class FilterForm(forms.Form):
	max_price = forms.IntegerField(label='Max Price:', required=False)
	pet_friendly = forms.BooleanField(label='Pet Friendly', required=False)
# has_dishwasher = forms.BooleanField(label='Has Dishwasher', required=False)
# has_laundry = forms.BooleanField(label='Has On-site Laundry', required=False)
# has_air_conditioning = forms.BooleanField(label='Has Air Conditioning', required=False)
