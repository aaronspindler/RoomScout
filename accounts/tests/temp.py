def test_verification_view_authenticated(self):
	print('Testing accounts.views.verification() authenticated')
	self.client.login(username='FredFlintstone', password='babadoo')


# response = self.client.get(reverse('settings_verification'))
# self.assertEqual(response.status_code, 200)

def test_verification_view_unauthenticated(self):
	print('Testing accounts.views.verification() unauthenticated')


# response = self.client.get(reverse('settings_verification'))
# self.assertEqual(response.status_code, 302)

def test_email_unsubscribe_view_authenticated(self):
	print('Testing accounts.views.unsubscribe() authenticated')


def test_email_unsubscribe_view_unauthenticated(self):
	print('Testing accounts.views.unsubscribe() unauthenticated')
