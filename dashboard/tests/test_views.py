from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class DashboardViewsTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')
	
	def test_dashboard_views_main_dashboard_get(self):
		print('Testing dashboard.views.main_dashboard() GET')
		self.client.force_login(self.user)
		response = self.client.get(reverse('main_dashboard'), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'dashboard/main_dashboard.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_dashboard_views_main_dashboard_get_not_logged_in(self):
		print('Testing dashboard.views.main_dashboard() GET not logged in')
		self.client.logout()
		response = self.client.get(reverse('main_dashboard'), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')

