from django.test import TestCase
from utils.datetime import *
import datetime

class DateTimeTest(TestCase):
    def test_now(self):
        now_sample = now()
        self.assertEqual(now_sample,datetime.datetime.now())
