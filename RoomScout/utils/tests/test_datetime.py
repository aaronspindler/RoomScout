from django.test import TestCase
from utils.datetime import *
import datetime

class DateTimeTest(TestCase):
    def test_now(self):
        print('Testing utils.datetime.now()')
        now_sample = now()
        self.assertEqual(now_sample,datetime.datetime.now())
