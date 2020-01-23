from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from bills.models import BillSet, Bill
from houses.models import House
from utils.models import BillFile


class BillsViewsTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')
		self.user2 = User.objects.create_user(username='JackyFlintstone', email='jacky@flintstone.com', password='lovefred')
		
		house = House.objects.create(user=self.user)
		house.place_id = 'EiwyNTI5IFN0YWxsaW9uIERyLCBPc2hhd2EsIE9OIEwxSCA3SzQsIENhbmFkYSIxEi8KFAoSCY_JD3vDG9WJEe3JFhlBvwOKEOETKhQKEgnrS9FlwxvViRHYx20MM9m-8g'
		house.lat = '43.95858010000001'
		house.lon = '-78.91587470000002'
		house.street_number = 2529
		house.street_name = 'Stallion Drive'
		house.city = 'Oshawa'
		house.prov_state = 'ON'
		house.postal_code = 'L1H 0M4'
		house.country = 'Canada'
		
		house.save()
		self.house = house
		
		self.billset = BillSet.objects.create(month=11, year=2019, house=self.house)
		self.bill = Bill.objects.create(set=self.billset, user=self.user, type='ELEC', date='2019-11-04', amount=299.99)
	
	def test_bill_delete_view_get(self):
		print('Testing bills.views.bill_delete() GET')
		self.client.force_login(self.user)
		bill_pre_count = Bill.objects.count()
		billset_pre_count = BillSet.objects.count()
		response = self.client.get(reverse('bill_delete', kwargs={'pk': self.bill.id}, ), follow=True)
		bill_post_count = Bill.objects.count()
		billset_post_count = BillSet.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_detail.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertEqual(bill_post_count, bill_pre_count)
		self.assertEqual(billset_post_count, billset_pre_count)
	
	def test_bill_delete_view_get_not_logged_in(self):
		print('Testing bills.views.bill_delete() GET not logged in')
		self.client.logout()
		bill_pre_count = Bill.objects.count()
		billset_pre_count = BillSet.objects.count()
		response = self.client.get(reverse('bill_delete', kwargs={'pk': self.bill.id}, ), follow=True)
		bill_post_count = Bill.objects.count()
		billset_post_count = BillSet.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')
		self.assertEqual(bill_post_count, bill_pre_count)
		self.assertEqual(billset_post_count, billset_pre_count)
	
	def test_bill_delete_view_get_wrong_user(self):
		print('Testing bills.views.bill_delete() GET wrong user')
		self.client.force_login(self.user2)
		bill_pre_count = Bill.objects.count()
		billset_pre_count = BillSet.objects.count()
		response = self.client.get(reverse('bill_delete', kwargs={'pk': self.bill.id}, ), follow=True)
		bill_post_count = Bill.objects.count()
		billset_post_count = BillSet.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/404.html')
		self.assertContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertEqual(bill_post_count, bill_pre_count)
		self.assertEqual(billset_post_count, billset_pre_count)
	
	def test_bill_delete_view_post(self):
		print('Testing bills.views.bill_delete() POST')
		self.client.force_login(self.user)
		self.bill2 = Bill.objects.create(set=self.billset, user=self.user, type='WATER', date='2019-11-04', amount=500.99)
		bill_pre_count = Bill.objects.count()
		billset_pre_count = BillSet.objects.count()
		response = self.client.post(reverse('bill_delete', kwargs={'pk': self.bill.id}, ), follow=True)
		bill_post_count = Bill.objects.count()
		billset_post_count = BillSet.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_detail.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertLess(bill_post_count, bill_pre_count)
		self.assertEqual(billset_post_count, billset_pre_count)
	
	def test_bill_delete_view_post_remove_empty_set(self):
		print('Testing bills.views.bill_delete() POST also remove empty billset')
		self.client.force_login(self.user)
		bill_pre_count = Bill.objects.count()
		billset_pre_count = BillSet.objects.count()
		response = self.client.post(reverse('bill_delete', kwargs={'pk': self.bill.id}, ), follow=True)
		bill_post_count = Bill.objects.count()
		billset_post_count = BillSet.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_detail.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertLess(bill_post_count, bill_pre_count)
		self.assertLess(billset_post_count, billset_pre_count)
	
	def test_bill_delete_view_post_not_logged_in(self):
		print('Testing bills.views.bill_delete() POST not logged in')
		self.client.logout()
		bill_pre_count = Bill.objects.count()
		billset_pre_count = BillSet.objects.count()
		response = self.client.post(reverse('bill_delete', kwargs={'pk': self.bill.id}, ), follow=True)
		bill_post_count = Bill.objects.count()
		billset_post_count = BillSet.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')
		self.assertEqual(bill_post_count, bill_pre_count)
		self.assertEqual(billset_post_count, billset_pre_count)
	
	def test_bill_delete_view_post_wrong_user(self):
		print('Testing bills.views.bill_delete() POST wrong user')
		self.client.force_login(self.user2)
		bill_pre_count = Bill.objects.count()
		billset_pre_count = BillSet.objects.count()
		response = self.client.post(reverse('bill_delete', kwargs={'pk': self.bill.id}, ), follow=True)
		bill_post_count = Bill.objects.count()
		billset_post_count = BillSet.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/404.html')
		self.assertContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertEqual(bill_post_count, bill_pre_count)
		self.assertEqual(billset_post_count, billset_pre_count)

	def test_bill_add_file_get(self):
		print('Testing bills.views.bill_add_file() GET')
		self.client.force_login(self.user)
		billfile_pre_count = BillFile.objects.count()
		response = self.client.get(reverse('bill_add_file', kwargs={'pk': self.bill.id}, ), follow=True)
		billfile_post_count = BillFile.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'bills/bill_add_file.html')
		self.assertContains(response, self.bill.set.house)
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertEqual(billfile_post_count, billfile_pre_count)

	def test_bill_add_file_get_not_logged_in(self):
		print('Testing bills.views.bill_add_file() GET not logged in')
		self.client.logout()
		billfile_pre_count = BillFile.objects.count()
		response = self.client.get(reverse('bill_add_file', kwargs={'pk': self.bill.id}, ), follow=True)
		billfile_post_count = BillFile.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, self.bill.set.house)
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')
		self.assertEqual(billfile_post_count, billfile_pre_count)

	def test_bill_add_file_get_wrong_user(self):
		print('Testing bills.views.bill_add_file() GET wrong user')
		self.client.force_login(self.user2)
		billfile_pre_count = BillFile.objects.count()
		response = self.client.get(reverse('bill_add_file', kwargs={'pk': self.bill.id}, ), follow=True)
		billfile_post_count = BillFile.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/404.html')
		self.assertNotContains(response, self.bill.set.house)
		self.assertContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertEqual(billfile_post_count, billfile_pre_count)