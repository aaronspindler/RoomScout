from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class HousesViewsTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')

	def test_house_create_page(self):
		print('Testing house creation page')
		self.client.login(username='Fred_Flintstone', password='foo')
		response = self.client.get(reverse('house_create'))
		self.assertEqual(response.status_code, 200)
