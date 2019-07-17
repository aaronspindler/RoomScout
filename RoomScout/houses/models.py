from django.db import models
from accounts.models import User
from django_countries.fields import CountryField
import uuid

class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

    address = models.CharField(max_length=400)
    country = CountryField(default='CA')
    prov_state = models.CharField(max_length = 2)
    postal_code = models.CharField(max_length = 7)
    date_posted = models.DateTimeField()
    kijiji_link = models.URLField(default="")
