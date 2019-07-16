from django.test import TestCase
from utils.uid import *

class UIDTestCase(TestCase):
    def test_create_uid(self):
        print('Testing utils.uid.create_uid()')
        uid_10 = []
        for x in range(10):
            uid_10.append(create_uid())

        for id in uid_10:
            self.assertEqual(len(id), 12)
