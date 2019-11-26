import boto3

from io import BytesIO
from random import randint
from PIL import ExifTags
from PIL import Image as Img
from django.conf import settings
from django.core.files import File
from django.db import models

from Roomscout.storage_backends import PrivateMediaStorage
from accounts.models import User
from bills.models import Bill
from houses.models import House
from rooms.models import Room


class IP(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	created = models.DateTimeField(auto_now=True)
	ip_address = models.GenericIPAddressField()


class PublicImage(models.Model):
	uploaded_at = models.DateTimeField(auto_now_add=True)
	is_approved = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField()

	def verify_image(self):
		client = boto3.client('rekognition', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, region_name='us-east-1')
		response = client.detect_moderation_labels(Image={'S3Object': {'Bucket': 'roomscout-public', 'Name': self.image.name}})
		if len(response['ModerationLabels']) > 0:
			self.is_approved = False
		else:
			self.is_approved = True
		super(PublicImage, self).save()

	def save(self, **kwargs):
		# This should only be checked if there is exif data
		if self.image:
			try:
				pilImage = Img.open(BytesIO(self.image.read()))
				for orientation in ExifTags.TAGS.keys():
					if ExifTags.TAGS[orientation] == 'Orientation':
						break
				exif = dict(pilImage._getexif().items())

				if exif[orientation] == 3:
					pilImage = pilImage.rotate(180, expand=True)
				elif exif[orientation] == 6:
					pilImage = pilImage.rotate(270, expand=True)
				elif exif[orientation] == 8:
					pilImage = pilImage.rotate(90, expand=True)

				output = BytesIO()
				pilImage.save()
				output.seek(0)
				self.image = File(output, self.image.name)
			except Exception:
				pass

		super(PublicImage, self).save()
		self.verify_image()


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
