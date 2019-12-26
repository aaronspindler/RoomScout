from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from bills.models import BillSet, Bill
from houses.models import House


class BillsModelTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='aaron@xnovax.net', password='babadoo')
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
	
	def test_BillSet_creation(self):
		print('Testing BillSet creation')
		pre_count = BillSet.objects.count()
		billset = BillSet()
		billset.month = 10
		billset.year = 2019
		billset.house = self.house
		billset.save()
		post_count = BillSet.objects.count()
		self.assertGreater(post_count, pre_count)
		self.assertEqual(billset.get_month_name(), 'October')
		self.assertEqual(billset.__str__(), 'October 2019')
	
	def test_Bill_creation(self):
		billset = BillSet()
		billset.month = 10
		billset.year = 2019
		billset.house = self.house
		billset.save()
		
		pre_count = Bill.objects.count()
		bill = Bill()
		bill.set = billset
		bill.user = self.user
		bill.type = 'ELEC'
		bill.date = '2019-11-04'
		bill.amount = 199.99
		bill.save()
		post_count = Bill.objects.count()
		self.assertGreater(post_count, pre_count)