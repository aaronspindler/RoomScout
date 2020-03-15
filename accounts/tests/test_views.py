from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import User


class AccountsViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')

    def test_settings_view_authenticated_get(self):
        print('Testing accounts.views.settings() GET authenticated')
        self.client.login(username='FredFlintstone', password='babadoo')
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/settings.html')
        self.assertContains(response, 'Settings')

    def test_settings_view_authenticated_post(self):
        print('Testing accounts.views.settings() POST authenticated')
        self.client.login(username='FredFlintstone', password='babadoo')
        # Test Original Values
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')
        self.assertEqual(self.user.city, '')
        self.assertEqual(self.user.prov_state, '')
        self.assertEqual(self.user.gender, '')
        self.assertEqual(self.user.age, 0)

        req_data = {'first_name': 'Fred', 'last_name': 'Flintstone', 'city': 'Kingston', 'province': 'ON', 'age': 19, 'gender': 'm'}
        response = self.client.post(reverse('settings'), req_data)
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.get(username='FredFlintstone')
        self.assertEqual(self.user.first_name, 'Fred')
        self.assertEqual(self.user.last_name, 'Flintstone')
        self.assertEqual(self.user.city, 'Kingston')
        self.assertEqual(self.user.prov_state, 'ON')
        self.assertEqual(self.user.gender, 'm')
        self.assertEqual(self.user.age, 19)

    def test_settings_view_authenticated_post_bad(self):
        print('Testing accounts.views.settings() INVALID POST authenticated')
        self.client.login(username='FredFlintstone', password='babadoo')
        # Test Original Values
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')
        self.assertEqual(self.user.city, '')
        self.assertEqual(self.user.prov_state, '')
        self.assertEqual(self.user.gender, '')
        self.assertEqual(self.user.age, 0)

        req_data = {'first_name': '', 'last_name': '', 'city': '', 'province': '', 'age': '', 'gender': ''}
        response = self.client.post(reverse('settings'), req_data)
        self.assertEqual(response.status_code, 302)

    def test_settings_view_unauthenticated_get(self):
        print('Testing accounts.views.settings() GET unauthenticated')
        self.client.logout()
        response = self.client.get(reverse('settings'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertNotContains(response, 'Settings')
        self.assertContains(response, 'Login')
        self.assertTemplateUsed(response, 'account/login.html')

    def test_preferences_view_authenticated_get(self):
        print('Testing accounts.views.preferences() GET authenticated')
        self.client.login(username='FredFlintstone', password='babadoo')
        response = self.client.get(reverse('settings_preferences'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertContains(response, 'Settings')
        self.assertNotContains(response, 'Login')

    def test_preferences_view_unauthenticated_get(self):
        print('Testing accounts.views.preferences() GET unauthenticated')
        self.client.logout()
        response = self.client.get(reverse('settings_preferences'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertNotContains(response, 'Settings')
        self.assertContains(response, 'Login')
        self.assertTemplateUsed(response, 'account/login.html')

    def test_preferences_view_authenticated_post(self):
        print('Testing accounts.views.preferences() POST authenticated')
        self.client.login(username='FredFlintstone', password='babadoo')
        self.assertFalse(self.user.general_contact)
        self.assertFalse(self.user.promo_contact)

        req_data = {'general_contact': True, 'promo_contact': True}
        response = self.client.post(reverse('settings_preferences'), req_data)
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.get(username='FredFlintstone')
        self.assertTrue(self.user.general_contact)
        self.assertTrue(self.user.promo_contact)

    def test_verification_view_authenticated_get(self):
        print('Testing accounts.views.verification() GET authenticated')
        self.client.login(username='FredFlintstone', password='babadoo')
        response = self.client.get(reverse('settings_verification'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertContains(response, 'Settings')
        self.assertNotContains(response, 'Login')

    def test_verification_view_unauthenticated_get(self):
        print('Testing accounts.views.verification() GET unauthenticated')
        self.client.logout()
        response = self.client.get(reverse('settings_verification'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertNotContains(response, 'Settings')
        self.assertContains(response, 'Login')
        self.assertTemplateUsed(response, 'account/login.html')

    def test_verification_view_authenticated_post(self):
        print('Testing accounts.views.verification() POST authenticated')
        self.client.login(username='FredFlintstone', password='babadoo')
        self.assertEqual(self.user.phone_number, '')

        req_data = {'phone_number': '6139297722'}
        response = self.client.post(reverse('settings_verification'), req_data)
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.get(username='FredFlintstone')
        self.assertEqual(self.user.phone_number, '6139297722')

    def test_email_unsubscribe_view_authenticated_get(self):
        print('Testing accounts.views.unsubscribe() GET authenticated')
        self.client.login(username='FredFlintstone', password='babadoo')
        response = self.client.get(reverse('email_unsubscribe'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertContains(response, 'Settings')
        self.assertNotContains(response, 'Login')

    def test_email_unsubscribe_view_unauthenticated_get(self):
        print('Testing accounts.views.unsubscribe() GET unauthenticated')
        self.client.logout()
        response = self.client.get(reverse('email_unsubscribe'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertNotContains(response, 'Settings')
        self.assertContains(response, 'Login')
        self.assertTemplateUsed(response, 'account/login.html')
