from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address = models.CharField(default = '', max_length=400)
    country = CountryField(null=True)
    prov_state = models.CharField(default = '', max_length = 40)
    postal_code = models.CharField(default = '', max_length = 6)
    score = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
