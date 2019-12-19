from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from houses.models import House


class RoomsViewTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='aaron@xnovax.net', password='babadoo')
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

	def test_rooms_views_room_saved_get(self):
		print('Testing rooms.views.room_saved() GET')
		self.client.force_login(self.user)
		response = self.client.get(reverse('bill_delete', kwargs={'pk': self.bill.id}, ), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'rooms/room_saved.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertContains(response, 'Saved Rooms')
		self.assertNotContains(response, "Looks like you haven't saved any rooms yet!")

	def test_rooms_views_room_saved_get_empty(self):
		print('Testing rooms.views.room_saved() GET empty')
		self.client.force_login(self.user)
		response = self.client.get(reverse('room_saved'), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'rooms/room_saved.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertContains(response, 'Saved Rooms')
		self.assertContains(response, "Looks like you haven't saved any rooms yet!")

	def test_rooms_views_room_saved_get_not_logged_in(self):
		print('Testing rooms.views.room_saved() GET not logged in')
		self.client.logout()
		response = self.client.get(reverse('room_saved'), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')
		self.assertNotContains(response, 'Saved Rooms')
		self.assertNotContains(response, "Looks like you haven't saved any rooms yet!")
