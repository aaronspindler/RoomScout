from django.db import models
from accounts.models import User
from django_countries.fields import CountryField
from utils.datetime import now
from accounts.models import User

class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=400)
    country = CountryField()
    prov_state = models.CharField(max_length = 2)
    postal_code = models.CharField(max_length = 6)
    date_posted = models.DateTimeField(default=now())
    kijiji_link = models.URLField(default="")
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    price = models.FloatField(default=0.0)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE,default='')

    image = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)
