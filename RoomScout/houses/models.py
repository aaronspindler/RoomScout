from django.db import models
from accounts.models import User
from django_countries.fields import CountryField
import uuid

class House(models.Model):

    prov_state_choices = (
        ('ON', 'Ontario'),
        ('QC','Quebec'),
        ('NS','Nova Scotia'),
        ('NB','New Brunswick'),
        ('MB','Manitoba'),
        ('BC','British Columbia'),
        ('PE','Prince Edward Island'),
        ('SK','Saskatchewan'),
        ('AB','Alberta'),
        ('NL','Newfoundland & Labrador'),
        ('NA','Not Applicable')
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    address = models.CharField(max_length=400)
    country = CountryField(default='CA')
    city = models.CharField(max_length=400, default='')
    prov_state = models.CharField(max_length = 2, choices=prov_state_choices)
    postal_code = models.CharField(max_length = 7, default='')

    hide_address = models.BooleanField(default=False)

    def full_address(self):
        return '{}, {}, {}, {}, {}'.format(self.address, self.city, self.prov_state, self.country.name, self.postal_code)
