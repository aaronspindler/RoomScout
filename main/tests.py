# Create your tests here.
from django.urls import reverse
from django.test import TestCase


class PageTests(TestCase):
	def test_home_view(self):
		print("Testing main.views.home()")
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'RoomScout')
		self.assertNotContains(response, 'This should not be contained!')
		self.assertTemplateUsed(response, 'main/home.html')

	def test_about_view(self):
		print("Testing main.views.about()")
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'About')
		self.assertNotContains(response, 'This should not be contained!')
		self.assertTemplateUsed(response, 'main/about.html')

	def test_contactus_view(self):
		print("Testing main.views.contactus()")
		response = self.client.get(reverse('contactus'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Contact')
		self.assertNotContains(response, 'This should not be contained!')
		self.assertTemplateUsed(response, 'main/contactus.html')

	def test_licenses_view(self):
		print("Testing main.views.licenses()")
		response = self.client.get(reverse('licenses'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Licenses')
		self.assertNotContains(response, 'This should not be contained!')
		self.assertTemplateUsed(response, 'main/licenses.html')

	def test_privacypolicy_view(self):
		print("Testing main.views.privacypolicy()")
		response = self.client.get(reverse('privacypolicy'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Privacy Policy')
		self.assertNotContains(response, 'This should not be contained!')
		self.assertTemplateUsed(response, 'main/privacypolicy.html')

	def test_termsofuse_view(self):
		print("Testing main.views.termsofuse()")
		response = self.client.get(reverse('termsofuse'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Terms of Use')
		self.assertNotContains(response, 'This should not be contained!')
		self.assertTemplateUsed(response, 'main/termsofuse.html')