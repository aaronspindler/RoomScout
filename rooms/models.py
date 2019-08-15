from django.db import models

from accounts.models import User
from houses.models import House


class Room(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	name = models.CharField(max_length=200, default='')
	is_available = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house')

	price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

	def __str__(self):
		return self.name
