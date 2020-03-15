from django.contrib.auth import get_user_model
from django.templatetags.static import static
from django.test import TestCase, Client

from houses.models import House
from rooms.models import Room, Inquiry, RoomLike


class RoomsModelTests(TestCase):
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

    def test_room_creation_blank(self):
        print('Testing rooms.models.Room creation blank')
        pre_count = Room.objects.count()
        room = Room.objects.create(user=self.user, house=self.house)
        post_count = Room.objects.count()
        self.assertGreater(post_count, pre_count)
        self.assertTrue(room.is_available)
        self.assertEqual(room.__str__(), room.name)
        self.assertEqual(room.get_first_image(), static('logos/logo.PNG'))

    def test_room_creation_filled(self):
        print('Testing rooms.models.Room creation filled')
        pre_count = Room.objects.count()
        room = Room.objects.create(user=self.user, house=self.house)
        room.price = 799.99
        room.name = "Master Bedroom"
        room.description = "Looking for a student tenant"
        room.is_accessible = False
        room.open_to_students = True
        room.pet_friendly = True
        room.utilities_included = True
        room.parking = True
        room.furnished = False
        room.female_only = False
        room.save()

        post_count = Room.objects.count()
        self.assertGreater(post_count, pre_count)
        self.assertEqual(room.price, 799.99)
        self.assertEqual(room.name, 'Master Bedroom')
        self.assertEqual(room.description, 'Looking for a student tenant')
        self.assertFalse(room.is_accessible)
        self.assertTrue(room.open_to_students)
        self.assertTrue(room.pet_friendly)
        self.assertTrue(room.utilities_included)
        self.assertTrue(room.parking)
        self.assertFalse(room.furnished)
        self.assertFalse(room.female_only)

        self.assertEqual(room.__str__(), room.name)
        self.assertEqual(room.get_first_image(), static('logos/logo.PNG'))
        self.assertEqual(room.get_time_difference_display(), 'Less than 1 hour ago')


class InquiryModelTests(TestCase):
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

        room = Room.objects.create(user=self.user, house=self.house)
        room.price = 799.99
        room.name = "Master Bedroom"
        room.description = "Looking for a student tenant"
        room.is_accessible = False
        room.open_to_students = True
        room.pet_friendly = True
        room.utilities_included = True
        room.parking = True
        room.furnished = False
        room.female_only = False
        room.save()

        self.room = room

    def test_inquiry_creation_blank(self):
        print('Testing rooms.models.Inquiry creation blank')
        pre_count = Inquiry.objects.count()
        inquiry = Inquiry.objects.create(user=self.user, room=self.room)
        post_count = Inquiry.objects.count()
        self.assertGreater(post_count, pre_count)

    def test_inquiry_creation_filled(self):
        print('Testing rooms.models.Inquiry creation filled')
        pre_count = Inquiry.objects.count()
        inquiry = Inquiry.objects.create(user=self.user, room=self.room, message='I am interested in this room!', move_in_date='2019-11-04')
        post_count = Inquiry.objects.count()
        self.assertGreater(post_count, pre_count)
        self.assertEqual(inquiry.status, 'O')


class RoomLikeModelTests(TestCase):
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

        room = Room.objects.create(user=self.user, house=self.house)
        room.price = 799.99
        room.name = "Master Bedroom"
        room.description = "Looking for a student tenant"
        room.is_accessible = False
        room.open_to_students = True
        room.pet_friendly = True
        room.utilities_included = True
        room.parking = True
        room.furnished = False
        room.female_only = False
        room.save()

        self.room = room

    def test_roomlike_creation(self):
        print('Testing rooms.models.RoomLike creation')
        pre_count = RoomLike.objects.count()
        roomlike = RoomLike.objects.create(room=self.room, user=self.user)
        post_count = RoomLike.objects.count()
        self.assertGreater(post_count, pre_count)
