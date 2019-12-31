from django.contrib import admin

from .models import Bill, BillSet


class BillAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'amount', 'user')


class BillSetAdmin(admin.ModelAdmin):
    list_display = ('house', 'month', 'year')


admin.site.register(Bill, BillAdmin)
admin.site.register(BillSet, BillSetAdmin)
