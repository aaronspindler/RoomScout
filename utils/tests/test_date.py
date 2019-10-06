from django.test import TestCase

from utils.date import *


class DateTest(TestCase):

    def test_check_format(self):
        print('Testing utils.date.check_format()')
        self.assertEqual(check_format('1997-11-04'), True)
        self.assertEqual(check_format('1234/1234/1234'), False)
        self.assertEqual(check_format('11-04-1997'), False)
        self.assertEqual(check_format('11/04/1997'), False)
        self.assertEqual(check_format('1997/11/04'), False)