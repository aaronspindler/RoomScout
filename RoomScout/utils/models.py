import boto3
import time
from django.db import models
from django.conf import settings

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

	def check_image(self):
		print(self.image.name)
		client = boto3.client('rekognition', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
		                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, region_name='us-east-1')
		response = client.detect_moderation_labels(Image={'S3Object': {'Bucket': 'roomscout-public', 'Name': self.image.name}})
		if len(response['ModerationLabels']) > 0:
			self.is_approved = False
		else:
			self.is_approved = True
		super(PublicImage, self).save()
			
	def save(self):
		super(PublicImage, self).save()
		self.check_image()
		


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
