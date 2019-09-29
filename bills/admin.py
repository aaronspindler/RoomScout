from django.contrib import admin

from .models import Bill, BillSet

admin.site.register(Bill)
admin.site.register(BillSet)
