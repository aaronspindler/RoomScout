from django.db import models

from accounts.models import User


class House(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_approved = models.BooleanField(default=False)
	is_available = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	street_number = models.IntegerField(default=0)
	street_name = models.CharField(max_length=400, default='')
	city = models.CharField(max_length=400, default='')
	prov_state = models.CharField(max_length=2)
	postal_code = models.CharField(max_length=7, default='')
	country = models.CharField(max_length=100, default='')

	hide_address = models.BooleanField(default=False)

	def full_address(self):
		return '{} {}, {}, {}, {}, {}'.format(self.street_number, self.street_name, self.city, self.prov_state, self.country,
		                                   self.postal_code)
