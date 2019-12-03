from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from houses.models import House


class HousesViewsTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')
		self.user2 = User.objects.create_user(username='JackyFlintstone', email='jacky@flintstone.com', password='lovefred')
		house = House.objects.create(user=self.user)
		house.place_id = 'EiwyNTI5IFN0YWxsaW9uIERyLCBPc2hhd2EsIE9OIEwxSCA3SzQsIENhbmFkYSIxEi8KFAoSCY_JD3vDG9WJEe3JFhlBvwOKEOETKhQKEgnrS9FlwxvViRHYx20MM9m-8g'
		house.lat = '43.95858010000001'
		house.lon = '-78.91587470000002'
		house.street_number = 2529
		house.street_name = 'Stallion Drive'
		house.city = 'Oshawa'
		house.prov_state = 'ON'
		house.postal_code = 'L1H 0M4'
		house.country = 'Canada'

		house.save()
		self.house = house

	def test_house_add_room_view_get(self):
		pass
	def test_house_add_room_view_get_not_logged_in(self):
		pass
	def test_house_add_room_view_get_wrong_user(self):
		pass
	def test_house_add_room_view_post(self):
		pass
	def test_house_add_room_view_post_no_name(self):
		pass
	def test_house_add_room_view_post_no_price(self):
		pass
	def test_house_add_room_view_post_no_description(self):
		pass
	def test_house_add_room_view_post_not_logged_in(self):
		pass
	def test_house_add_room_view_post_wrong_user(self):
		pass


	def test_house_detail_view_get_valid(self):
		print('Testing houses.views.house_details() GET VALID')
		self.client.login(username='Fred_Flintstone', password='foo')
		response = self.client.get(reverse('house_detail', args=[self.house.id]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_detail.html')
		self.assertContains(response, self.house)

	def test_house_detail_view_get_valid1(self):
		print('Testing houses.views.house_details() GET VALID1')
		self.client.login(username='Fred_Flintstone', password='foo')
		response = self.client.get(self.house.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_detail.html')
		self.assertContains(response, self.house)

	def test_house_detail_view_get_invalidpk(self):
		print('Testing houses.views.house_details() GET INVALID PK')
		self.client.login(username='Fred_Flintstone', password='foo')
		response = self.client.get(reverse('house_detail', args=[-1]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/404.html')
		self.assertNotContains(response, 'Details')
		self.assertContains(response, '404')

	def test_house_edit_view_get(self):
		print('Testing houses.views.house_edit() GET')
		self.client.force_login(self.user)
		response = self.client.get(reverse('house_edit', args=[self.house.id]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_edit.html')
		self.assertContains(response, self.house)
		self.assertContains(response, 'Editing')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')

	def test_house_edit_view_get_not_logged_in(self):
		print('Testing houses.views.house_edit() GET not logged in')
		self.client.logout()
		response = self.client.get(reverse('house_edit', args=[self.house.id]), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Login')
		self.assertTemplateUsed(response, 'account/login.html')

	def test_house_edit_view_get_wrong_user(self):
		print('Testing houses.views.house_edit() GET wrong user')
		self.client.force_login(self.user2)
		response = self.client.get(reverse('house_edit', args=[self.house.id]), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '404')
		self.assertTemplateUsed(response, 'main/404.html')

	def test_house_edit_view_post(self):
		print('Testing houses.views.house_edit() POST')
		# Test before values
		self.assertFalse(self.house.hide_address)
		self.assertEqual(self.house.num_rooms, 0)
		self.assertEqual(self.house.num_bathrooms, 0)
		self.assertEqual(self.house.num_parking_spaces, 0)
		self.assertFalse(self.house.has_dishwasher)
		self.assertFalse(self.house.has_laundry)
		self.assertFalse(self.house.has_air_conditioning)

		req_data = {'hide_address': True, 'num_rooms': 4, 'num_bathrooms': 4, 'num_parking_spaces': 4, 'has_dishwasher': True, 'has_laundry': True, 'has_air_conditioning': True}
		self.client.force_login(self.user)
		response = self.client.post(reverse('house_edit', args=[self.house.id]), req_data, follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_detail.html')

		# Test post values
		self.house = House.objects.get(pk=self.house.id)
		self.assertTrue(self.house.hide_address)
		self.assertEqual(self.house.num_rooms, 4)
		self.assertEqual(self.house.num_bathrooms, 4)
		self.assertEqual(self.house.num_parking_spaces, 4)
		self.assertTrue(self.house.has_dishwasher)
		self.assertTrue(self.house.has_laundry)
		self.assertTrue(self.house.has_air_conditioning)

	def test_house_edit_view_post_wrong_user(self):
		print('Testing houses.views.house_edit() POST wrong user')
		# Test before values
		self.assertFalse(self.house.hide_address)
		self.assertEqual(self.house.num_rooms, 0)
		self.assertEqual(self.house.num_bathrooms, 0)
		self.assertEqual(self.house.num_parking_spaces, 0)
		self.assertFalse(self.house.has_dishwasher)
		self.assertFalse(self.house.has_laundry)
		self.assertFalse(self.house.has_air_conditioning)

		req_data = {'hide_address': True, 'num_rooms': 4, 'num_bathrooms': 4, 'num_parking_spaces': 4, 'has_dishwasher': True, 'has_laundry': True, 'has_air_conditioning': True}
		self.client.force_login(self.user2)
		response = self.client.post(reverse('house_edit', args=[self.house.id]), req_data, follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '404')
		self.assertTemplateUsed(response, 'main/404.html')

		# Test after values
		self.assertFalse(self.house.hide_address)
		self.assertEqual(self.house.num_rooms, 0)
		self.assertEqual(self.house.num_bathrooms, 0)
		self.assertEqual(self.house.num_parking_spaces, 0)
		self.assertFalse(self.house.has_dishwasher)
		self.assertFalse(self.house.has_laundry)
		self.assertFalse(self.house.has_air_conditioning)

	def test_house_delete_view_get(self):
		print('Testing houses.views.house_delete() GET')
		self.client.force_login(self.user)
		response = self.client.get(reverse('house_delete', args=[self.house.id]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_delete.html')
		self.assertContains(response, self.house)
		self.assertContains(response, 'Delete')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')

	def test_house_delete_view_get_not_logged_in(self):
		print('Testing houses.views.house_delete() GET not logged in')
		self.client.logout()
		response = self.client.get(reverse('house_delete', args=[self.house.id]), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Login')
		self.assertTemplateUsed(response, 'account/login.html')

	def test_house_delete_view_get_wrong_user(self):
		print('Testing houses.views.house_delete() GET wrong user')
		self.client.force_login(self.user2)
		response = self.client.get(reverse('house_delete', args=[self.house.id]), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '404')
		self.assertTemplateUsed(response, 'main/404.html')

	def test_house_delete_view_post(self):
		print('Testing houses.views.house_delete() POST')
		count_pre = House.objects.count()
		req_data = {}
		self.client.force_login(self.user)
		response = self.client.post(reverse('house_delete', args=[self.house.id]), req_data, follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'dashboard/main_dashboard.html')
		count_post = House.objects.count()
		self.assertEqual(count_pre-1, count_post)

	def test_house_delete_view_post_wrong_user(self):
		print('Testing houses.views.house_delete() POST wrong user')
		count_pre = House.objects.count()
		req_data = {}
		self.client.force_login(self.user2)
		response = self.client.post(reverse('house_delete', args=[self.house.id]), req_data, follow=True)
		count_post = House.objects.count()
		self.assertEqual(count_pre, count_post)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '404')
		self.assertTemplateUsed(response, 'main/404.html')

	def test_house_delete_view_post_not_logged_in(self):
		print('Testing houses.views.house_delete() POST not logged in')
		count_pre = House.objects.count()
		req_data = {}
		self.client.logout()
		response = self.client.post(reverse('house_delete', args=[self.house.id]), req_data, follow=True)
		count_post = House.objects.count()
		self.assertEqual(count_pre, count_post)
		self.assertEqual(response.status_code, 200)
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'DELETE')
		self.assertContains(response, 'Login')
		self.assertTemplateUsed(response, 'account/login.html')
