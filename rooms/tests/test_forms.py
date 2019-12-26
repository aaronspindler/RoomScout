from django.test import TestCase

from rooms.forms import FilterForm


class RoomsFormTests(TestCase):
    def test_filterform_valid(self):
        print('Testing rooms.forms.FilterForm Valid')
        form = FilterForm(
            data={'open_to_students': False, 'is_accessible': False, 'utilities_included': False, 'max_price': 0,
                  'pet_friendly': False, 'has_dishwasher': False, 'has_laundry': False, 'has_air_conditioning': False,
                  'order_by': '-updated_at'
                  }
        )
        self.assertTrue(form.is_valid())

    def test_filterform_valid1(self):
        print('Testing rooms.forms.FilterForm Valid 1')
        form = FilterForm(
            data={'open_to_students': True, 'is_accessible': True, 'utilities_included': True, 'max_price': 0,
                  'pet_friendly': True, 'has_dishwasher': True, 'has_laundry': True, 'has_air_conditioning': True,
                  'order_by': '-updated_at'
                  }
        )
        self.assertTrue(form.is_valid())

    def test_filterform_valid2(self):
        print('Testing rooms.forms.FilterForm Valid 2')
        form = FilterForm(
            data={'open_to_students': None, 'is_accessible': None, 'utilities_included': None, 'max_price': 0,
                  'pet_friendly': None, 'has_dishwasher': None, 'has_laundry': None, 'has_air_conditioning': None,
                  'order_by': '-updated_at'
                  }
        )
        self.assertTrue(form.is_valid())