from django.test import TestCase

from main.models import ContactMessage


class MainModelTests(TestCase):
    def test_main_models_ContactMessage(self):
        print('Testing main.models.ContactMessage() creation')
        pre_count = ContactMessage.objects.count()
        message = ContactMessage.objects.create(sender="aaron@spindlers.ca", subject='Test Message', message='Message Contents')
        post_count = ContactMessage.objects.count()
        self.assertGreater(post_count, pre_count)
