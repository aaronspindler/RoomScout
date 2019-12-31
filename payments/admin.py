from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'email', 'amount')


admin.site.register(Donation, DonationAdmin)
