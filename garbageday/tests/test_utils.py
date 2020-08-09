import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from garbageday.models import GarbageDay
from houses.models import House


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

        self.assertEquals(self.house.garbageday_set.count(), 0)

    def test_garbageday_utils_update_garbage_days_no_updated_needed(self):
        print('Testing garbageday.utils.update_garbage_days() No Update Needed')
        self.garbage_day = GarbageDay()
        self.garbage_day.house = self.house
        self.garbage_day.user = self.user
        self.garbage_day.last_garbage_day = datetime.date.today()
        self.garbage_day.next_garbage_day = datetime.date.today() + datetime.timedelta(days=14)
        print(self.garbage_day.last_garbage_day)
        print(self.garbage_day.next_garbage_day)

        self.garbage_day.save()
        print(self.garbage_day.last_updated)
        self.assertEquals(self.house.garbageday_set.count(), 1)
        self.assertEqual(self.house.garbageday_set.first().garbage_frequency, datetime.timedelta(days=14))
