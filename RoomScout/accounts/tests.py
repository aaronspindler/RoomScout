from django.test import TestCase

from .models import User


class LoginTest(TestCase):
	def test_login_view(self):
		print('Testing accounts.views.login')
		response = self.client.get('/accounts/login/')
		self.assertEqual(response.status_code, 200)

	def test_login_form_post(self):
		# Create user to login
		pre_count = User.objects.count()
		response = self.client.post('/accounts/signup/', {'email': 'Login@test.com', 'password1': 'django1234',
		                                        'password2': 'django1234'})
		post_count = User.objects.count()
		self.assertEqual(response.status_code, 302)
		self.assertEqual(pre_count + 1, post_count)

		print('Testing accounts.views.login POST : Invalid username/password')
		response = self.client.post('/accounts/login/', {'email': 'asdf1234@gmail.com', 'password': 'asdf1234'})
		self.assertEqual(response.status_code, 302)

		print('Testing accounts.views.login POST : Correct username/password')
		response = self.client.post('/accounts/login/', {'email': 'Login@test.com', 'password': 'django1234'})
		self.assertEqual(response.status_code, 302)


class SignupTest(TestCase):

	def test_signup_view(self):
		print('Testing accounts.views.signup')
		response = self.client.get('/accounts/signup/')
		self.assertEqual(response.status_code, 200)

	def test_signup_form_post_invalid(self):
		print('Testing accounts.views.signup POST Invalid : Form Empty')
		pre_count = User.objects.count()
		response = self.client.post('/accounts/signup/',{'email': '', 'password1': '', 'password2': ''})
		post_count = User.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(pre_count, post_count)


		print('Testing accounts.views.signup POST Invalid :  Empty Email')
		pre_count = User.objects.count()
		response = self.client.post('/accounts/signup/', {'email': '', 'password1': 'django1234', 'password2': 'django1234'})
		post_count = User.objects.count()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(pre_count, post_count)

	def test_signup_form_post_repeat(self):
		print('Testing accounts.views.signup POST : User Creation')
		# Create a user
		pre_count = User.objects.count()
		response = self.client.post('/accounts/signup/', {'email': 'aaron@xnovax.net', 'password1': 'django1234', 'password2': 'django1234'})
		post_count = User.objects.count()
		self.assertEqual(response.status_code, 302)
		self.assertEqual(pre_count + 1, post_count)

		print('Testing accounts.views.signup POST : Repeat Username')
		# Repeat user by username, shouldn't create another user
		pre_count = User.objects.count()
		response = self.client.post('/accounts/signup/', {'email': 'aaron@xnovax.net', 'password1': 'django1234','password2': 'django1234'})
		self.assertEqual(response.status_code, 302)
		post_count = User.objects.count()
		self.assertEqual(pre_count, post_count)

		print('Testing accounts.views.signup POST : Repeat Email')
		# Repeat user by email, shouldn't create another user
		pre_count = User.objects.count()
		response = self.client.post('/accounts/signup/', {'email': 'aaron@xnovax.net', 'password1': 'django1234', 'password2': 'django1234'})
		self.assertEqual(response.status_code, 302)
		post_count = User.objects.count()
		self.assertEqual(pre_count, post_count)
