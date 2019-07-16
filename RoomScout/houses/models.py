from django.db import models
from accounts.models import User
from django_countries.fields import CountryField
import uuid

class House(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    address = models.CharField(max_length=400)
    country = CountryField()
    prov_state = models.CharField(max_length = 2)
    postal_code = models.CharField(max_length = 6)
    date_posted = models.DateTimeField()
    kijiji_link = models.URLField(default="")
