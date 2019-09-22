# Create your tests here.
from django.test import TestCase

from .models import Room


class RoomTest(TestCase):
	def test_creation(self):
		print('Testing room creation')
		room = Room()
		#now_sample = now()
		#self.assertEqual(now_sample, datetime.datetime.now())
