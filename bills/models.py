from django.db import models

from accounts.models import User
from houses.models import House

class Bill(models.Model):
	TYPE_CHOICES = [('ElEC', 'Electricity'), ('WATER','Water'), ('GAS', 'Gas'), ('INTER','Internet'), ('OTHER', 'Other')]

	type = models.CharField(choices=TYPE_CHOICES, max_length=5)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	house = models.ForeignKey(House, on_delete=models.CASCADE)
	is_approved = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	date = models.DateField(auto_now=True)
	file = models.FileField(default=None)
	amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

class BillSet(models.Model):
	date = models.DateField(auto_now=True)
	pass