from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from houses.models import House, Invitation


class HousesModelTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')
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

	# Commented out because of API usage
	# def test_house_load_walk_score(self):
	#	print('Testing house.load_walk_score()')
	#	house = self.house_attributes
	#	self.assertEqual(house.postal_code, 'L1H 0M4')
	#   house.load_walk_score()
	#   self.assertEqual(house.walk_score, 0)
	#   self.assertEqual(house.walk_score_description, 'Car-Dependent')
	#   self.assertEqual(house.bike_score, 23)
	#   self.assertEqual(house.bike_score_description, 'Somewhat Bikeable')
	#   self.assertEqual(house.transit_score, -1)
	#   self.assertEqual(house.transit_score_description, '')
	#   self.assertEqual(house.transit_score_summary, '')

	def test_house_hide_address(self):
		print('Testing house.hide_address')
		self.assertEqual(self.house.full_address(), '2529 Stallion Drive, Oshawa, ON, Canada, L1H 0M4')
		self.house.hide_address = True
		self.house.save()
		self.assertEqual(self.house.full_address(), 'Stallion Drive, Oshawa, ON, Canada')

	def test_house_to_string(self):
		print('Testing house.__str__')
		self.assertEqual(self.house.__str__(), '2529 Stallion Drive, Oshawa, ON, Canada, L1H 0M4')
		self.house.postal_code = ''
		self.house.save()
		self.assertEqual(self.house.__str__(), '2529 Stallion Drive, Oshawa, ON, Canada')

	def test_house_get_bill_labels(self):
		print('Testing house.get_bill_labels()')
		self.assertEqual(len(self.house.get_bill_labels()), 0)

	def test_house_get_electricity_bills(self):
		print('Testing house.get_electricity_bills()')
		self.assertEqual(len(self.house.get_electricity_bills()), 0)

	def test_house_get_water_bills(self):
		print('Testing house.get_water_bills()')
		self.assertEqual(len(self.house.get_water_bills()), 0)

	def test_house_get_gas_bills(self):
		print('Testing house.get_gas_bills()')
		self.assertEqual(len(self.house.get_gas_bills()), 0)

	def test_house_get_internet_bills(self):
		print('Testing house.get_internet_bills()')
		self.assertEqual(len(self.house.get_internet_bills()), 0)

	def test_house_get_other_bills(self):
		print('Testing house.get_other_bills()')
		self.assertEqual(len(self.house.get_other_bills()), 0)

	def test_create_default_house(self):
		print('Testing house create default')
		house_count_pre = House.objects.count()
		house = House.objects.create(user=self.user)
		house.save()
		house_count_post = House.objects.count()
		self.assertEqual(house_count_post, house_count_pre + 1)

		self.assertEqual(house.members.count(), 0)
		self.assertFalse(house.is_approved)
		self.assertFalse(house.is_available)
		self.assertEqual(house.place_id, '')
		self.assertEqual(house.lat, '')
		self.assertEqual(house.lon, '')
		self.assertEqual(house.street_number, '')
		self.assertEqual(house.street_name, '')
		self.assertEqual(house.city, '')
		self.assertEqual(house.prov_state, '')
		self.assertEqual(house.postal_code, '')
		self.assertEqual(house.country, '')

		self.assertEqual(house.num_rooms, 0)
		self.assertEqual(house.num_bathrooms, 0)
		self.assertEqual(house.num_parking_spaces, 0)
		self.assertFalse(house.has_dishwasher)
		self.assertFalse(house.has_laundry)
		self.assertFalse(house.has_air_conditioning)

		self.assertFalse(house.hide_address)


class InvitationModelTests(TestCase):
	def setUp(self):
		print('Invitation setup')
		User = get_user_model()
		user = User.objects.create_user(username='Fred_Flintstone', email='normal@user.com', password='foo')
		self.user = user
		self.house = House.objects.create(user=self.user)

	def test_invitation_creation(self):
		print('Testing Invitation Creation')
		count_prior = Invitation.objects.all().count()
		fixture = Invitation()
		fixture.target = 'Aaron@xnovax.net'
		fixture.sender = self.user
		fixture.house = self.house
		fixture.save()
		count_after = Invitation.objects.all().count()
		self.assertEqual(count_prior + 1, count_after)
