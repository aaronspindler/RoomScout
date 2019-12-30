from django.test import TestCase
from accounts.forms import PreferencesForm, VerificationForm


class AccountsFormsTests(TestCase):
	def test_PreferencesForm_valid(self):
		print('Testing accounts.forms.PreferencesForm VALID')
		form = PreferencesForm(data={'general_contact': True, 'promo_contact': True})
		self.assertTrue(form.is_valid())

	def test_PreferencesForm_valid1(self):
		print('Testing accounts.forms.PreferencesForm VALID 1')
		form = PreferencesForm(data={'general_contact': False, 'promo_contact': False})
		self.assertTrue(form.is_valid())

	def test_PreferencesForm_valid2(self):
		print('Testing accounts.forms.PreferencesForm VALID 2')
		form = PreferencesForm(data={'general_contact': False, 'promo_contact': True})
		self.assertTrue(form.is_valid())

	def test_PreferencesForm_valid3(self):
		print('Testing accounts.forms.PreferencesForm VALID 3')
		form = PreferencesForm(data={'general_contact': True, 'promo_contact': False})
		self.assertTrue(form.is_valid())

	def test_VerificationForm_valid(self):
		print('Testing accounts.forms.VerficiationForm VALID')
		form = VerificationForm(data={'phone_number': '12345678911234567891'})
		self.assertTrue(form.is_valid())

	def test_VerificationForm_valid1(self):
		print('Testing accounts.forms.VerficiationForm VALID 1')
		form = VerificationForm(data={'phone_number': '6139297722'})
		self.assertTrue(form.is_valid())

	def test_VerificationForm_valid2(self):
		print('Testing accounts.forms.VerficiationForm VALID 2')
		form = VerificationForm(data={'phone_number': '+1(613)-929-7722'})
		self.assertTrue(form.is_valid())

	def test_VerificationForm_invalid(self):
		print('Testing accounts.forms.VerficiationForm INVALID')
		form = VerificationForm(data={'phone_number': '12345678911234567891111'})
		self.assertFalse(form.is_valid())