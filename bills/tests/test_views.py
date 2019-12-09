from django.contrib.auth import get_user_model
from django.test import TestCase, Client


class BillsViewsTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')
		self.user2 = User.objects.create_user(username='JackyFlintstone', email='jacky@flintstone.com', password='lovefred')
	
	def test_bill_delete_view_get(self):
		print('Testing bills.views.bill_delete(pk) GET')
		self.client.force_login(self.user)
	
	def test_bill_delete_view_get_not_logged_in(self):
		print('Testing bills.views.bill_delete(pk) GET not logged in')
		self.client.logout()
	
	def test_bill_delete_view_get_wrong_user(self):
		print('Testing bills.views.bill_delete(pk) GET wrong user')
		self.client.force_login(self.user2)
	
	def test_bill_delete_view_post(self):
		print('Testing bills.views.bill_delete(pk) POST')
		self.client.force_login(self.user)
	
	def test_bill_delete_view_post_not_logged_in(self):
		print('Testing bills.views.bill_delete(pk) POST not logged in')
		self.client.logout()
	
	def test_bill_delete_view_post_wrong_user(self):
		print('Testing bills.views.bill_delete(pk) POST wrong user')
		self.client.force_login(self.user2)