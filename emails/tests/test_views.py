from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class EmailsViewsTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')