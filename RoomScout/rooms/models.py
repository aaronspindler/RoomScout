from django.db import models

from accounts.models import User
from houses.models import House


class Room(models.Model):
	name = models.CharField(max_length=200, default='')
	is_available = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house')

	price = models.FloatField(default=0.0)
