from django.contrib import admin

from .models import IP, RoomImage, HouseImage, BillFile, PhoneNumberVerification


class IPAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'created')


class RoomImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'image', 'is_approved')


class HouseImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'house', 'image', 'is_approved')


class BillFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'file')


class PhoneNumberVerificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(IP, IPAdmin)
admin.site.register(RoomImage, RoomImageAdmin)
admin.site.register(HouseImage, HouseImageAdmin)
admin.site.register(BillFile, BillFileAdmin)
admin.site.register(PhoneNumberVerification, PhoneNumberVerificationAdmin)
