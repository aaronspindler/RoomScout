from django import forms


class FilterForm(forms.Form):
	SORT_CHOICES = (
		('-updated_at', 'Newest First'),
		('updated_at', 'Oldest First'),
		('-price', 'Highest Price First'),
		('price', 'Lowest Price First')
	)

	open_to_students = forms.BooleanField(label='Open to students', required=False)
	is_accessible = forms.BooleanField(label='Accessible', required=False)
	utilities_included = forms.BooleanField(label='Utilities Included', required=False)
	max_price = forms.IntegerField(label='Max Price:', required=False)
	pet_friendly = forms.BooleanField(label='Pet Friendly', required=False)
	has_dishwasher = forms.BooleanField(label='Has Dishwasher', required=False)
	has_laundry = forms.BooleanField(label='Has On-site Laundry', required=False)
	has_air_conditioning = forms.BooleanField(label='Has Air Conditioning', required=False)
	order_by = forms.ChoiceField(choices=SORT_CHOICES, label='Sort By', required=False, initial='-updated_at')
