from django.db import models
from datetime import datetime

from accounts.models import User
from houses.models import House


class GarbageDay(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	house = models.OneToOneField(House, on_delete=models.CASCADE)

	# User Inputted
	last_garbage_day = models.DateField()
	next_garbage_day = models.DateField()

	# Generated
	garbage_frequency = models.DurationField(null=True)

	def calculate_garbage_frequency(self):
		delta = datetime.strptime(self.next_garbage_day, '%Y-%m-%d') - datetime.strptime(self.last_garbage_day, '%Y-%m-%d')
		self.garbage_frequency = delta

	def save(self, **kwargs):
		self.calculate_garbage_frequency()
		super(GarbageDay, self).save()

