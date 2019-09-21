from random import randint

import boto3
from django.db import models
from django.conf import settings

from Roomscout.storage_backends import PrivateMediaStorage
from accounts.models import User
from rooms.models import Room
from houses.models import House
from bills.models import Bill


class IP(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	created = models.DateTimeField(auto_now=True)
	ip_address = models.GenericIPAddressField()


class PublicImage(models.Model):
	uploaded_at = models.DateTimeField(auto_now_add=True)
	is_approved = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField()

	def check_image(self):
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
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(storage=PrivateMediaStorage())


class RoomImage(PublicImage):
	room = models.ForeignKey(Room, on_delete=models.CASCADE)

class HouseImage(PublicImage):
	house = models.ForeignKey(House, on_delete=models.CASCADE)

class PrivateFile(models.Model):
	uploaded_at = models.DateTimeField(auto_now_add=True)
	is_approved = models.BooleanField(default=False)
	file = models.FileField(storage=PrivateMediaStorage())
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class BillFile(PrivateFile):
	bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

class PhoneNumberVerification(models.Model):
	phone_number = models.IntegerField(default=-1)
	code = models.IntegerField(default=-1)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def generate_code(self):
		self.code = randint(10000, 99999)

