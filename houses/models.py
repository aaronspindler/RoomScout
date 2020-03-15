import uuid
from decimal import Decimal

import requests
from django.conf import settings
from django.db import models
from django.urls import reverse

from accounts.models import User


class House(models.Model):
    # Generated Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members')
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Location Information
    place_id = models.TextField(default='')
    lat = models.TextField(default='')
    lon = models.TextField(default='')
    street_number = models.CharField(max_length=400, default='')
    street_name = models.CharField(max_length=400, default='')
    city = models.CharField(max_length=400, default='')
    prov_state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=7, default='')
    country = models.CharField(max_length=100, default='')

    # Walk Score
    walk_scores_updated = models.DateTimeField(auto_now=True)
    walk_score = models.IntegerField(default=-1)
    walk_score_description = models.TextField(default='')
    bike_score = models.IntegerField(default=-1)
    bike_score_description = models.TextField(default='')
    transit_score = models.IntegerField(default=-1)
    transit_score_description = models.TextField(default='')
    transit_score_summary = models.TextField(default='')

    # Filterable Options
    # TODO: Implement these options into house
    num_rooms = models.IntegerField(default=0, verbose_name='Number of Rooms')
    num_bathrooms = models.IntegerField(default=0, verbose_name='Number of Bathrooms')
    num_parking_spaces = models.IntegerField(default=0, verbose_name='Number of Parking Spaces')
    has_dishwasher = models.BooleanField(default=False)
    has_laundry = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)

    # Used to hide the address from public consumption
    # Changes all full_address postings to use a non specific address
    # Eg 2529 Stallion Dr, Oshawa, Ontario, Canada will become Stallion Dr, Oshawa, Ontario, Canada
    hide_address = models.BooleanField(default=False, help_text="Hides the specific address on all publicly available pages")

    # Loads walk score information from walkscore.com
    # This should only be ran when the house in created on our backend and very infrequently after
    # Walk score information does not update very often
    # and we only have 5000 daily API calls
    # Todo: Implement a monitor for counting number of calls per day
    def load_walk_score(self):
        url = 'http://api.walkscore.com/score?format=json&address={address}&lat={lat}&lon={lon}&transit=1&bike=1&wsapikey={api_key}'.format(address=self.full_address(), lat=self.lat, lon=self.lon, api_key=settings.WALK_SCORE_API)
        response = requests.get(url)
        json = response.json()
        if json['status'] == 1:
            self.walk_score = json['walkscore']
            self.walk_score_description = json['description']
            self.walk_scores_updated = json['updated']

            try:
                self.transit_score = json['transit']['score']
                self.transit_score_description = json['transit']['description']
                self.transit_score_summary = json['transit']['summary']
            except Exception:
                pass

            try:
                self.bike_score = json['bike']['score']
                self.bike_score_description = json['bike']['description']
            except Exception:
                pass
            self.save()

    def __str__(self):
        return self.full_address()

    def get_absolute_url(self):
        return reverse('house_detail', args=[str(self.pk)])

    def full_address(self):
        if self.hide_address:
            return '{}, {}, {}, {}'.format(self.street_name, self.city, self.prov_state, self.country)
        if self.postal_code:
            return '{} {}, {}, {}, {}, {}'.format(self.street_number, self.street_name, self.city, self.prov_state, self.country, self.postal_code)
        else:
            return '{} {}, {}, {}, {}'.format(self.street_number, self.street_name, self.city, self.prov_state, self.country)

    def get_bill_labels(self):
        labels = []
        billsets = self.billset_set.all()
        for billset in billsets:
            labels.append(billset.get_month_name() + ' ' + str(billset.year))
        return labels

    # TODO: Refactor to make this simpler and more robust
    def get_bills(self, type):
        bills = []
        billsets = self.billset_set.all()
        for billset in billsets:
            bill_type = billset.bill_set.filter(type=type)
            sum = Decimal(0.0)
            for bill in bill_type:
                sum += bill.amount
            bills.append(sum.__str__())
        return bills

    def get_electricity_bills(self):
        return self.get_bills('ELEC')

    def get_water_bills(self):
        return self.get_bills('WATER')

    def get_gas_bills(self):
        return self.get_bills('GAS')

    def get_internet_bills(self):
        return self.get_bills('INTER')

    def get_other_bills(self):
        return self.get_bills('OTHER')


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    target = models.EmailField(default='')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
