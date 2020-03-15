from django.test import TestCase

from utils.provinces import *


class ProvincesTestCase(TestCase):
    def test_get_provinces(self):
        print('Testing utils.provinces.get_provinces()')
        provinces = get_provinces()
        self.assertEqual(len(provinces), 11)
