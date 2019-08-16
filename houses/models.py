from django.db import models
from django.conf import settings
import requests

from accounts.models import User


class House(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_approved = models.BooleanField(default=False)
	is_available = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	place_id = models.TextField(default='')
	lat = models.TextField(default='')
	lon = models.TextField(default='')
	street_number = models.IntegerField(default=0)
	street_name = models.CharField(max_length=400, default='')
	city = models.CharField(max_length=400, default='')
	prov_state = models.CharField(max_length=2)
	postal_code = models.CharField(max_length=7, default='')
	country = models.CharField(max_length=100, default='')

	walk_score = models.IntegerField(default=0)
	bike_score = models.IntegerField(default=0)
	transit_score = models.IntegerField(default=0)

	hide_address = models.BooleanField(default=False)

	def encode_address(self):
		pass

	def load_walk_score(self):
		url = 'http://api.walkscore.com/score?format=json&address={address}&lat={lat}&lon={lon}&transit=1&bike=1&wsapikey={api_key}'.format(address=self.encode_address(), lat=self.lat, lon=self.lon, api_key=settings.WALK_SCORE_API)
		response = requests.get(url)
		# Receive Request
		if response['status'] == 1:

			# Parse Request
			pass

	def __str__(self):
		return self.full_address()

	def full_address(self):
		if self.postal_code:
			return '{} {}, {}, {}, {}, {}'.format(self.street_number, self.street_name, self.city, self.prov_state, self.country,self.postal_code)
		else:
			return '{} {}, {}, {}, {}'.format(self.street_number, self.street_name, self.city, self.prov_state,
												  self.country)
