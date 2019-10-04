from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	GENDER_CHOICES = [('m', 'Male'), ('f', 'Female'), ('o', 'Other')]

	# Contact
	phone_number = models.CharField(max_length=20, default='')
	phone_number_verified = models.BooleanField(default=False)

	# Address
	city = models.CharField(default='', max_length=200)
	prov_state = models.CharField(default='', max_length=2)

	# User Data
	gender = models.CharField(choices=GENDER_CHOICES, default='', max_length=2)
	age = models.IntegerField(default=0)

	# Contact Consent
	general_contact = models.BooleanField(default=False)
	promo_contact = models.BooleanField(default=False)

	# Generated Fields
	_score = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
	is_premium_member = models.BooleanField(default=True)

	# Premium Features
	max_houses = models.IntegerField(default=1)

	# Returns true if the majority of profile is filled out
	def profile_filled(self):
		num_fields = 2
		num_filled = 0

		if self.gender != '':
			num_filled += 1
		if self.age != 0:
			num_filled += 1

		if num_filled >= (num_fields / 3):
			return True
		return False

	def get_score(self):
		return self._score