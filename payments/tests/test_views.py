from django.test import TestCase
from django.urls import reverse


class PaymentsViewTests(TestCase):
	def test_payments_views_payment_donation_get(self):
		print('Testing payments.views.payment_donation() GET')
		response = self.client.get(reverse('payment_donation', kwargs={'amount': 100}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'RoomScout')
		self.assertNotContains(response, 'This should not be contained!')
		self.assertContains(response, 'Support Us')
		self.assertNotContains(response, 404)
		self.assertTemplateUsed(response, 'main/supportus.html')
	
	
	def test_payments_views_payment_donation_post(self):
		print('Testing payments.views.payment_donation() POST')
		# TODO: Figure out a way to mock stripe token

