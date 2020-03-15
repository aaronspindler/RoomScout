from django.test import TestCase

from emails.models import EmailMessage


class EmailsModelTests(TestCase):
    def test_Emails_EmailMessage_model_creation(self):
        print('Testing emails.models.EmailMessage creation')
        pre_count = EmailMessage.objects.count()
        email = EmailMessage.objects.create(from_email='Aaron@xnovax.net', to_email='Aaron@Spindlers.ca', subject='This is a test email', text_content='This is a tester email, please ignore it! Aaron Spindler', html_content="<h1>This is a tester email, please ignore it! Aaron Spindler</h1>")
        post_count = EmailMessage.objects.count()
        self.assertGreater(post_count, pre_count)
        self.assertEqual(email.from_email, 'Aaron@xnovax.net')
        self.assertEqual(email.to_email, 'Aaron@Spindlers.ca')
        self.assertEqual(email.subject, 'This is a test email')
        self.assertEqual(email.text_content, 'This is a tester email, please ignore it! Aaron Spindler')
        self.assertEqual(email.html_content, '<h1>This is a tester email, please ignore it! Aaron Spindler</h1>')
