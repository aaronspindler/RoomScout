from django.contrib.auth import get_user_model
from django.test import TestCase


class BillsTests(TestCase):
	def setUp(self):
		User = get_user_model()
		user = User.objects.create_user(username='Fred_Flintstone', email='normal@user.com', password='foo')
		self.assertEqual(user.email, 'normal@user.com')
		self.assertEqual(user.username, 'Fred_Flintstone')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)
