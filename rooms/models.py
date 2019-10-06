from django.db import models
from django.urls import reverse

from accounts.models import User
from houses.models import House
from utils.datetime import time_diff_display


class Room(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, default='')
	description = models.TextField(default='')
	is_available = models.BooleanField(verbose_name='Available', default=True , help_text='Room is available')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	is_accessible = models.BooleanField(default=False, verbose_name="Accessible", help_text="House is accessible with ramp or elevator")
	open_to_students = models.BooleanField(default=True, help_text="Students are free to inquire about rooms at this house")
	pet_friendly = models.BooleanField(default=False, help_text="Pets are allowed")
	utilities_included = models.BooleanField(default=False, help_text="All utilities are included in the price of rent")
	parking = models.BooleanField(default=False, help_text="Parking spot is included or available")
	furnished = models.BooleanField(default=False, help_text="Room is furnished with at least a bed, mattress, and dresser")
	female_only = models.BooleanField(default=False, help_text="Only females are allowed to inquire")

	house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house')

	price = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('room_detail', args=[str(self.pk)])

	def get_time_difference_display(self):
		return time_diff_display(self.updated_at)

	def get_first_image(self):
		room_images = self.roomimage_set
		if room_images.count() > 0:
			return room_images.first().image.url

		house_images = self.house.houseimage_set
		if house_images.count() > 0:
			return house_images.first().image.url



class Inquiry(models.Model):
	STATUS_CHOICES = [('O', 'Open'), ('D', 'Dismissed')]
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	message = models.TextField(default='')
	move_in_date = models.DateField(default='1997-11-04')
	status = models.CharField(choices=STATUS_CHOICES, default='O', max_length=3)
