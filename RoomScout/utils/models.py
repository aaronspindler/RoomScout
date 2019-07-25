from django.db import models
from accounts.models import User
from rooms.models import Room

class Email(models.Model):
	sent_at = models.DateTimeField(auto_now_add=True)
	sent_to = models.EmailField()
	subject = models.TextField()
	contents = models.TextField()

class IP(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	created = models.DateTimeField(auto_now=True)
	ip_address = models.GenericIPAddressField()

class Image(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	image = models.ImageField(upload_to='images/', blank=True)

class RoomImage(Image):
	room = models.ForeignKey(Room, on_delete=models.PROTECT)
