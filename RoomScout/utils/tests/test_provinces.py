from django.test import TestCase
from utils.provinces import *

class ProvincesTestCase(TestCase):
    def test_now(self):
        provinces = get_provinces()
        self.assertEqual(len(provinces),11)
