from datetime import datetime

from django.db import models

from accounts.models import User
from houses.models import House


class GarbageDay(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    last_updated = models.DateField(auto_now_add=True, null=True)

    # User Inputted
    last_garbage_day = models.DateField()
    next_garbage_day = models.DateField()

    # Generated
    garbage_frequency = models.DurationField(null=True, blank=True)

    def calculate_garbage_frequency(self):
        if type(self.next_garbage_day) == str and type(self.last_garbage_day) == str:
            delta = datetime.strptime(self.next_garbage_day, '%Y-%m-%d') - datetime.strptime(self.last_garbage_day, '%Y-%m-%d')
        else:
            delta = self.next_garbage_day - self.last_garbage_day
        self.garbage_frequency = delta

    def save(self, **kwargs):
        self.calculate_garbage_frequency()
        super(GarbageDay, self).save()
