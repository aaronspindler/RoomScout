from django.contrib.auth import get_user_model
from django.test import TestCase
from datetime import timedelta

from houses.models import House
from .models import GarbageDay


class GarbageDayTests(TestCase):
	def setUp(self):
		User = get_user_model()
		user = User.objects.create_user(username='Fred_Flintstone', email='normal@user.com', password='foo')
		self.user = user
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

	def test_create_garbage_day1(self):
		print('Testing GarbageDay Creation Blank')
		num_pre = GarbageDay.objects.count()
		garbage_day = GarbageDay()
		garbage_day.house = self.house
		garbage_day.user = self.user
		garbage_day.last_garbage_day = "2019-11-04"
		garbage_day.next_garbage_day = "2019-11-04"
		garbage_day.save()
		self.assertEqual(garbage_day.house, self.house)
		num_post = GarbageDay.objects.count()
		self.assertEqual(num_post, num_pre + 1)
		self.assertEqual(garbage_day.garbage_frequency, timedelta(weeks=0, days=0))

	def test_create_garbage_day2(self):
		print('Testing GarbageDay Creation Filled')
		num_pre = GarbageDay.objects.count()
		garbage_day = GarbageDay()
		garbage_day.house = self.house
		garbage_day.user = self.user
		garbage_day.last_garbage_day = "2019-11-12"
		garbage_day.next_garbage_day = "2019-11-26"
		garbage_day.save()
		self.assertEqual(garbage_day.house, self.house)
		num_post = GarbageDay.objects.count()
		self.assertEqual(num_post, num_pre + 1)
		self.assertEqual(garbage_day.garbage_frequency, timedelta(weeks=2, days=0))

	def test_garbage_day_house_relation(self):
		print('Testing GarbageDay House Relation')
		garbage_day = GarbageDay()
		garbage_day.house = self.house
		garbage_day.user = self.user
		garbage_day.last_garbage_day = "2019-11-12"
		garbage_day.next_garbage_day = "2019-11-26"
		garbage_day.save()
		self.assertIsNot(self.house.garbageday_set.count(), 0)