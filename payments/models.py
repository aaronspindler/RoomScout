from django.db import models


class Donation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    email = models.EmailField()
