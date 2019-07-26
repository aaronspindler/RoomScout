from django.db import models

from RoomScout.storage_backends import PrivateMediaStorage
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


class PublicImage(models.Model):
	uploaded_at = models.DateTimeField(auto_now_add=True)
	is_approved = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	image = models.ImageField()


class PrivateImage(models.Model):
	uploaded_at = models.DateTimeField(auto_now_add=True)
	is_approved = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	image = models.ImageField(storage=PrivateMediaStorage())


class RoomImage(PublicImage):
	room = models.ForeignKey(Room, on_delete=models.PROTECT)


class PrivateFile(models.Model):
	uploaded_at = models.DateTimeField(auto_now_add=True)
	is_approved = models.BooleanField(default=False)
	upload = models.FileField(storage=PrivateMediaStorage())
	user = models.ForeignKey(User, on_delete=models.PROTECT)
