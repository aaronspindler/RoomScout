from django.db import models

from accounts.models import User
from houses.models import House


class BillSet(models.Model):
    month = models.IntegerField(default=-1)
    year = models.IntegerField(default=-1)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_month_name() + ' ' + str(self.year)

    def get_month_name(self):
        months = ["Unknown",
                  "January",
                  "Febuary",
                  "March",
                  "April",
                  "May",
                  "June",
                  "July",
                  "August",
                  "September",
                  "October",
                  "November",
                  "December"]
        if self.month < 1 or self.month > 12:
            return 'Error'
        return months[self.month]

    def get_total(self):
        total = 0
        bills = Bill.objects.filter(set=self)
        for bill in bills:
            total += bill.amount
        return total

    # TODO: This needs to be reworked to account for the owner if living in house and if members haven't registered yet. Maybe use a number in the house for the bill split multiplier
    def get_total_per_person(self):
        return self.get_total() / self.house.members.count()

    class Meta:
        ordering = ['year', 'month']


class Bill(models.Model):
    TYPE_CHOICES = [('ELEC', 'Electricity'), ('WATER', 'Water'), ('GAS', 'Gas'), ('INTER', 'Internet'), ('OTHER', 'Other')]

    set = models.ForeignKey(BillSet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    type = models.CharField(choices=TYPE_CHOICES, max_length=5)
    date = models.DateField()
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    
    class Meta:
        ordering = ['date']
