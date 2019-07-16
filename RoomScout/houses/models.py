from django.db import models
from accounts.models import User
from django_countries.fields import CountryField
from accounts.models import User

class House(models.Model):
    key = models.CharField(primary_key=True, max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    address = models.CharField(max_length=400)
    country = CountryField()
    prov_state = models.CharField(max_length = 2)
    postal_code = models.CharField(max_length = 6)
    date_posted = models.DateTimeField()
    kijiji_link = models.URLField(default="")

class Room(models.Model):
    key = models.CharField(primary_key=True, max_length=12)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE,default='')

    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)
