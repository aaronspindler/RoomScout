from django.test import TestCase
from datetime import timedelta, datetime


class GarbageDayTests(TestCase):
	def test_garbageday_calculate_garbage_frequency(self):
		print('Testing GarbageDay.calculate_garbage_frequency()')
		house = self.house_attributes
		self.assertEqual(house.garbage_frequency, timedelta(0))
		house.calculate_garbage_frequency()
		self.assertEqual(house.garbage_frequency, timedelta(weeks=2, days=0))