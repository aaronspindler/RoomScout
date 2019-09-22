from datetime import datetime, timedelta

from django.test import TestCase

from utils.datetime import *


class DateTimeTest(TestCase):
	def test_now(self):
		print('Testing utils.datetime.now()')
		now_sample = now()
		self.assertEqual(now_sample, datetime.datetime.now())

	def test_time_diff_display(self):
		print('Testing utils.datetime.time_diff_display()')
		updated_0min_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=0, minutes=0)
		self.assertEqual(time_diff_display(updated_0min_ago), 'Less than 1 hour ago')
		updated_1min_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=0, minutes=1)
		self.assertEqual(time_diff_display(updated_1min_ago), 'Less than 1 hour ago')
		updated_59min_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=0, minutes=59)
		self.assertEqual(time_diff_display(updated_59min_ago), 'Less than 1 hour ago')
		updated_1hr_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=1, minutes=0)
		self.assertEqual(time_diff_display(updated_1hr_ago), "1 hour ago")
		updated_2hr_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=2, minutes=0)
		self.assertEqual(time_diff_display(updated_2hr_ago), "2 hours ago")
		updated_1day_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=24, minutes=0)
		self.assertEqual(time_diff_display(updated_1day_ago), "1 day ago")
		updated_10days_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=240, minutes=0)
		self.assertEqual(time_diff_display(updated_10days_ago), "10 days ago")
		updated_30days_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=720, minutes=0)
		self.assertEqual(time_diff_display(updated_30days_ago), "30 days ago")
		updated_90days_ago = datetime.datetime.now(datetime.timezone.utc) - timedelta(hours=2160, minutes=0)
		self.assertEqual(time_diff_display(updated_90days_ago), "90 days ago")
