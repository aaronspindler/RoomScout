from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
	phone_number = PhoneNumberField(blank=True)
	phone_number_confirmed = models.BooleanField(default=False)
	address = models.TextField(default='')
	city = models.CharField(default='', max_length=200)
	prov_state = models.CharField(default='', max_length=2)
	postal_code = models.CharField(default='', max_length=7)
	score = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
