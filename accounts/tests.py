from django.test import TestCase
from django.contrib.auth import get_user_model

class AccountsTests(TestCase):
	def test_create_user(self):
		print('Testing accounts user creation')
		User = get_user_model()
		user = User.objects.create_user(username='Fred_Flintstone',email='normal@user.com', password='foo')
		self.assertEqual(user.email, 'normal@user.com')
		self.assertEqual(user.username, 'Fred_Flintstone')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)

	def test_create_superuser(self):
		print('Testing accounts super user creation')
		User = get_user_model()
		admin_user = User.objects.create_superuser(username='SuperFred_Flintstone',email='super@user.com', password='foo')
		self.assertEqual(admin_user.email, 'super@user.com')
		self.assertEqual(admin_user.username, 'SuperFred_Flintstone')
		self.assertTrue(admin_user.is_active)
		self.assertTrue(admin_user.is_staff)
		self.assertTrue(admin_user.is_superuser)

	def test_create_user_with_attributes(self):
		print('Testing accounts user creation with attributes')
		User = get_user_model()
		user = User.objects.create_user(username='user1', email='normal@user1.com', password='foo')
		user.first_name = 'Fred'
		user.last_name = 'Flintstone'
		user.phone_number = '6132276515'
		user.city = 'Kingston'
		user.prov_state = 'ON'
		user.gender = 'm'
		user.age = 21
		user.save()

		self.assertEqual(user.first_name, 'Fred')
		self.assertEqual(user.last_name, 'Flintstone')
		self.assertEqual(user.get_full_name(), 'Fred Flintstone')
		self.assertEqual(user.phone_number, '6132276515')
		self.assertEqual(user.city, 'Kingston')
		self.assertEqual(user.prov_state, 'ON')
		self.assertEqual(user.gender, 'm')
		self.assertEqual(user.age, 21)
		self.assertEqual(user.score, 0)
		self.assertEqual(user.max_houses, 1)

	def test_create_user_without_attributes(self):
		print('Testing accounts user creation without attributes')
		User = get_user_model()
		user = User.objects.create_user(username='user1', email='normal@user1.com', password='foo')
		user.save()

		self.assertNotEqual(user.first_name, 'Fred')
		self.assertNotEqual(user.last_name, 'Flintstone')
		self.assertNotEqual(user.get_full_name(), 'Fred Flintstone')
		self.assertNotEqual(user.phone_number, '6132276515')
		self.assertNotEqual(user.city, 'Kingston')
		self.assertNotEqual(user.prov_state, 'ON')
		self.assertNotEqual(user.gender, 'm')
		self.assertNotEqual(user.age, 21)
		self.assertEqual(user.score, 0)
		self.assertEqual(user.max_houses, 1)
