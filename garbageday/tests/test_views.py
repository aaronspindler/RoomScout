from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from houses.models import House
from garbageday.models import GarbageDay


class GarbageDayViewTests(TestCase):
	def setUp(self):
		User = get_user_model()
		self.user = User.objects.create_user(username='Fred_Flintstone', email='normal@user.com', password='foo')
		self.user2 = User.objects.create_user(username='JackyFlintstone', email='jacky@flintstone.com', password='lovefred')
		self.assertEqual(self.user.email, 'normal@user.com')
		self.assertEqual(self.user.username, 'Fred_Flintstone')
		self.assertTrue(self.user.is_active)
		self.assertFalse(self.user.is_staff)
		self.assertFalse(self.user.is_superuser)
		
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
	
	def test_garbageday_views_garbageday_manage_get_not_existing(self):
		print('Testing garbageday.views.garbageday_manage() GET not existing')
		self.client.force_login(self.user)
		count = GarbageDay.objects.filter(house=self.house).count()
		self.assertEqual(count, 0)
		response = self.client.get(reverse('garbageday_manage', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'garbageday/garbageday_create.html')
		self.assertContains(response, 'Setup Garbage Day for')
		self.assertContains(response, self.house)
		self.assertContains(response, 'Garbage Day')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		
	def test_garbageday_views_garbageday_manage_get_existing(self):
		print('Testing garbageday.views.garbageday_manage() GET existing')
		self.client.force_login(self.user)
		self.garbage_day = GarbageDay()
		self.garbage_day.house = self.house
		self.garbage_day.user = self.user
		self.garbage_day.last_garbage_day = "2019-11-12"
		self.garbage_day.next_garbage_day = "2019-11-26"
		self.garbage_day.save()
		count = GarbageDay.objects.filter(house=self.house).count()
		self.assertEqual(count, 1)
		response = self.client.get(reverse('garbageday_manage', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'garbageday/garbageday_edit.html')
		self.assertContains(response, 'Edit Garbage Day for')
		self.assertContains(response, self.house)
		self.assertContains(response, 'Garbage Day')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_manage_get_not_logged_in(self):
		print('Testing garbageday.views.garbageday_manage() GET not logged in')
		self.client.logout()
		response = self.client.get(reverse('garbageday_manage', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, 'Setup Garbage Day for')
		self.assertNotContains(response, self.house)
		self.assertNotContains(response, 'Garbage Day')
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')
	
	def test_garbageday_views_garbageday_manage_get_wrong_user(self):
		print('Testing garbageday.views.garbageday_manage() GET wrong user')
		self.client.force_login(self.user2)
		response = self.client.get(reverse('garbageday_manage', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/404.html')
		self.assertNotContains(response, 'Setup Garbage Day for')
		self.assertNotContains(response, self.house)
		self.assertNotContains(response, 'Garbage Day')
		self.assertContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_create_get(self):
		print('Testing garbageday.views.garbageday_create() GET')
		self.client.force_login(self.user)
		response = self.client.get(reverse('garbageday_create', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'garbageday/garbageday_create.html')
		self.assertContains(response, 'Setup Garbage Day for')
		self.assertContains(response, self.house)
		self.assertContains(response, 'Garbage Day')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_create_get_not_logged_in(self):
		print('Testing garbageday.views.garbageday_create() GET not logged in')
		self.client.logout()
		response = self.client.get(reverse('garbageday_create', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, 'Setup Garbage Day for')
		self.assertNotContains(response, self.house)
		self.assertNotContains(response, 'Garbage Day')
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')
	
	def test_garbageday_views_garbageday_create_get_wrong_user(self):
		print('Testing garbageday.views.garbageday_create() GET wrong user')
		self.client.force_login(self.user2)
		response = self.client.get(reverse('garbageday_create', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/404.html')
		self.assertNotContains(response, 'Setup Garbage Day for')
		self.assertNotContains(response, self.house)
		self.assertNotContains(response, 'Garbage Day')
		self.assertContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_create_post(self):
		print('Testing garbageday.views.garbageday_create() POST')
		self.client.force_login(self.user)
		pre_count = GarbageDay.objects.count()
		req_data = {'LastGarbageDay': '2019-11-12', 'NextGarbageDay': '2019-11-26'}
		response = self.client.post(reverse('garbageday_create', kwargs={'house': self.house.id}), req_data, follow=True)
		post_count = GarbageDay.objects.count()
		self.assertGreater(post_count, pre_count)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_detail.html')
		self.assertNotContains(response, 'Setup Garbage Day for')
		self.assertContains(response, self.house)
		self.assertContains(response, 'Garbage Day')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_create_post_existing(self):
		print('Testing garbageday.views.garbageday_create() POST existing')
		self.client.force_login(self.user)
		self.garbage_day = GarbageDay()
		self.garbage_day.house = self.house
		self.garbage_day.user = self.user
		self.garbage_day.last_garbage_day = "2019-11-12"
		self.garbage_day.next_garbage_day = "2019-11-26"
		self.garbage_day.save()
		
		pre_count = GarbageDay.objects.count()
		req_data = {'LastGarbageDay': '2019-11-12', 'NextGarbageDay': '2019-11-26'}
		response = self.client.post(reverse('garbageday_create', kwargs={'house': self.house.id}), req_data, follow=True)
		post_count = GarbageDay.objects.count()
		self.assertEqual(post_count, pre_count)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'houses/house_detail.html')
		self.assertNotContains(response, 'Setup Garbage Day for')
		self.assertContains(response, self.house)
		self.assertContains(response, 'Garbage Day')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_create_post_not_logged_in(self):
		print('Testing garbageday.views.garbageday_create() POST not logged in')
		self.client.logout()
		pre_count = GarbageDay.objects.count()
		req_data = {'LastGarbageDay': '2019-11-12', 'NextGarbageDay': '2019-11-26'}
		response = self.client.post(reverse('garbageday_create', kwargs={'house': self.house.id}), req_data, follow=True)
		post_count = GarbageDay.objects.count()
		self.assertEqual(post_count, pre_count)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, 'Setup Garbage Day for')
		self.assertNotContains(response, self.house)
		self.assertNotContains(response, 'Garbage Day')
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')
	
	def test_garbageday_views_garbageday_create_post_wrong_user(self):
		print('Testing garbageday.views.garbageday_create() POST wrong user')
		self.client.force_login(self.user2)
		pre_count = GarbageDay.objects.count()
		req_data = {'LastGarbageDay': '2019-11-12', 'NextGarbageDay': '2019-11-26'}
		response = self.client.post(reverse('garbageday_create', kwargs={'house': self.house.id}), req_data, follow=True)
		post_count = GarbageDay.objects.count()
		self.assertEqual(post_count, pre_count)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/404.html')
		self.assertNotContains(response, 'Setup Garbage Day for')
		self.assertNotContains(response, self.house)
		self.assertNotContains(response, 'Garbage Day')
		self.assertContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_edit_get(self):
		print('Testing garbageday.views.garbageday_edit() GET')
		self.client.force_login(self.user)
		response = self.client.get(reverse('garbageday_edit', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'garbageday/garbageday_edit.html')
		self.assertContains(response, 'Edit Garbage Day for')
		self.assertContains(response, self.house)
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_edit_get_not_logged_in(self):
		print('Testing garbageday.views.garbageday_edit() GET not logged in')
		self.client.logout()
		response = self.client.get(reverse('garbageday_edit', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/login.html')
		self.assertNotContains(response, 'Edit Garbage Day for')
		self.assertNotContains(response, self.house)
		self.assertNotContains(response, '404')
		self.assertContains(response, 'Login')
	
	def test_garbageday_views_garbageday_edit_get_wrong_user(self):
		print('Testing garbageday.views.garbageday_edit() GET wrong user')
		self.client.force_login(self.user2)
		response = self.client.get(reverse('garbageday_edit', kwargs={'house': self.house.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/404.html')
		self.assertNotContains(response, 'Edit Garbage Day for')
		self.assertNotContains(response, self.house)
		self.assertContains(response, '404')
		self.assertNotContains(response, 'Login')
	
	def test_garbageday_views_garbageday_edit_post(self):
		print('Testing garbageday.views.garbageday_edit() POST')
		self.client.force_login(self.user)
	
	def test_garbageday_views_garbageday_edit_post_not_logged_in(self):
		print('Testing garbageday.views.garbageday_edit() POST not logged in')
		self.client.logout()
	
	def test_garbageday_views_garbageday_edit_post_wrong_user(self):
		print('Testing garbageday.views.garbageday_edit() POST wrong user')
		self.client.force_login(self.user2)