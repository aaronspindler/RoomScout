from django.contrib.auth import get_user_model
from django.test import TestCase

from houses.models import House
from utils.models import HouseImage
from utils.streetview import load_house_image


class StreetViewTestCase(TestCase):

	def setUp(self):
		print('StreetView Testing Setup')
		User = get_user_model()
		user = User.objects.create_user(username='Fred_Flintstone', email='normal@user.com', password='foo')
		self.user = user

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

	def test_load_house_image(self):
		print('Testing utils.streetview.load_house_image(house)')
		pre_count = HouseImage.objects.count()
		load_house_image(self.house)
		post_count = HouseImage.objects.count()
		self.assertEqual(pre_count+1, post_count)
