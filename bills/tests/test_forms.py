from django.test import TestCase

from bills.forms import BillForm, BillFormset


class BillFormTests(TestCase):
    def test_BillForm_creation_valid(self):
        print('Testing bills.forms.BillForm() creation valid')
        form = BillForm({'date': '2019-11-04', 'type': 'ELEC', 'amount': 193.33})
        self.assertTrue(form.is_valid())

    def test_BillForm_creation_invalid(self):
        print('Testing bills.forms.BillForm() creation invalid')
        form = BillForm({'date': '', 'type': '', 'amount': -100})
        self.assertFalse(form.is_valid())


class BillFormsetTests(TestCase):
    def test_BillFormset_creation_valid(self):
        print('Testing bills.forms.BillFormset() creation valid')
        formset = BillFormset(
            {
                'form-INITIAL_FORMS': '0',
                'form-TOTAL_FORMS': '1',
                'form-0-date': '2019-11-04',
                'form-0-type': 'ELEC',
                'form-0-amount': 299.99,
                'form-0-file': None
            }
        )
        self.assertTrue(formset.is_valid())

    def test_BillFormset_creation_invalid(self):
        print('Testing bills.forms.BillFormset() creation invalid')
        formset = BillFormset(
            {
                'form-INITIAL_FORMS': '0',
                'form-TOTAL_FORMS': '2',
                'form-0-date': '',
                'form-0-type': '',
                'form-0-amount': -100,
                'form-0-file': None
            }
        )
        self.assertFalse(formset.is_valid())
