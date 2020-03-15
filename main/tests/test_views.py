from django.test import TestCase
from django.urls import reverse

from main.models import ContactMessage


class MainViewsTests(TestCase):
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

    def test_contactus_view_get(self):
        print("Testing main.views.contactus() GET")
        response = self.client.get(reverse('contactus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact')
        self.assertNotContains(response, 'This should not be contained!')
        self.assertTemplateUsed(response, 'main/contactus.html')

    def test_contactus_view_post(self):
        print("Testing main.views.contactus() POST")
        pre_count = ContactMessage.objects.count()
        req_data = {'sender_email': 'aaron@xnovax.net', 'subject': 'Contact Us Test', 'message': 'This is a test message!'}
        response = self.client.post(reverse('contactus'), req_data, follow=True)
        post_count = ContactMessage.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, 'We have received your contact request and will get back to you as soon as possible!')
        self.assertNotContains(response, '404')
        self.assertGreater(post_count, pre_count)

    def test_billfeatures_view(self):
        print("Testing main.views.billfeatures()")
        response = self.client.get(reverse('billfeatures'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bill Features')
        self.assertNotContains(response, 'This should not be contained!')
        self.assertTemplateUsed(response, 'main/billfeatures.html')

    def test_supportus_view(self):
        print("Testing main.views.supportus()")
        response = self.client.get(reverse('supportus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Support Us')
        self.assertNotContains(response, 'This should not be contained!')
        self.assertTemplateUsed(response, 'main/supportus.html')

    def test_verificationfeatures_view(self):
        print("Testing main.views.verificationfeatures()")
        response = self.client.get(reverse('verificationfeatures'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Verification Feature')
        self.assertNotContains(response, 'This should not be contained!')
        self.assertTemplateUsed(response, 'main/verificationfeatures.html')

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

    def test_sandbox_view(self):
        print("Testing main.views.sandbox()")
        response = self.client.get(reverse('sandbox'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Sandbox')
        self.assertTemplateUsed(response, 'account/login.html')
