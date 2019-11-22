from django.db import models


class Donation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    email = models.EmailField()
