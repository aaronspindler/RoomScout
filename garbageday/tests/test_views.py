from django.test import TestCase
from django.contrib.auth import get_user_model

from houses.models import House
from garbageday.models import GarbageDay


class GarbageDayViewTests(TestCase):
	def setUp(self):
		User = get_user_model()
		self.user = User.objects.create_user(username='Fred_Flintstone', email='normal@user.com', password='foo')
		self.user2 = User.objects.create_user(username='JackyFlintstone', email='jacky@flintstone.com', password='lovefred')
		self.assertEqual(self.user.email, 'normal@user.com')
		self.assertEqual(self.user.username, 'Fred_Flintstone')
		self.assertTrue(self.user.is_active)
		self.assertFalse(self.user.is_staff)
		self.assertFalse(self.user.is_superuser)
		
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
	
		
	def test_garbageday_views_garbageday_manage_get_not_existing(self):
		print('Testing garbageday.views.garbageday_manage GET not existing')
		self.client.force_login(self.user)
	
	def test_garbageday_views_garbageday_manage_get_existing(self):
		print('Testing garbageday.views.garbageday_manage GET existing')
		self.client.force_login(self.user)
	
	def test_garbageday_views_garbageday_manage_get_not_logged_in(self):
		print('Testing garbageday.views.garbageday_manage GET not logged in')
		self.client.logout()
	
	def test_garbageday_views_garbageday_manage_get_wrong_user(self):
		print('Testing garbageday.views.garbageday_manage GET wrong user')
		self.client.force_login(self.user2)