from django.db import models
from accounts.models import User
from houses.models import House

class Room(models.Model):
    name = models.CharField(max_length=200, default='')
    is_available = models.BooleanField(default=True)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE,default='')

    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)
