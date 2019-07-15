from django.db import models
from accounts.models import User
from django_countries.fields import CountryField

class Tenant(models.Model):
    pass

class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=400)
    country = CountryField()
    prov_state = models.CharField(max_length = 2)
    postal_code = models.CharField(max_length = 6)
    date_posted = models.DateTimeField(default=None)
    kijiji_link = models.URLField(default=None)

class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    image = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)
