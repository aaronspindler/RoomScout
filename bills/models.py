from django.db import models

from accounts.models import User
from houses.models import House

class BillSet(models.Model):
	month = models.IntegerField(default=-1)
	year = models.IntegerField(default=-1)
	house = models.ForeignKey(House, on_delete=models.CASCADE)

	def get_month_name(self):
		months = ["Unknown",
		          "January",
		          "Febuary",
		          "March",
		          "April",
		          "May",
		          "June",
		          "July",
		          "August",
		          "September",
		          "October",
		          "November",
		          "December"]
		if self.month < 1 or self.month > 12:
			return 'Error'
		return months[self.month]

class Bill(models.Model):
	TYPE_CHOICES = [('ElEC', 'Electricity'), ('WATER','Water'), ('GAS', 'Gas'), ('INTER','Internet'), ('OTHER', 'Other')]

	set = models.ForeignKey(BillSet, on_delete=models.CASCADE)
	type = models.CharField(choices=TYPE_CHOICES, max_length=5)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_approved = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	date = models.DateField(auto_now=True)
	file = models.FileField(default=None)
	amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

