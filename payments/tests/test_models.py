from django.test import TestCase

from payments.models import Donation


class PaymentsModelTests(TestCase):
	def test_payments_models_Donation_creation(self):
		print('Testing payment.models.Donation creation')
		pre_count = Donation.objects.count()
		donation = Donation.objects.create(amount=200.00, email='Fred@Flintstone.com')
		post_count = Donation.objects.count()
		self.assertGreater(post_count, pre_count)
	
	def test_payments_models_Donation_creation1(self):
		print('Testing payment.models.Donation creation 1')
		pre_count = Donation.objects.count()
		donation = Donation.objects.create(amount=200, email='Fred@Flintstone.com')
		post_count = Donation.objects.count()
		self.assertGreater(post_count, pre_count)
		