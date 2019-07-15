from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    score = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
