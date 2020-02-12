from django.contrib import admin

from .models import RoomImage, HouseImage, BillFile, PhoneNumberVerification, Fingerprint, BannedFingerprint


class RoomImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'image', 'is_approved')


class HouseImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'house', 'image', 'is_approved')


class BillFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'file')


class PhoneNumberVerificationAdmin(admin.ModelAdmin):
    pass


class FingerprintAdmin(admin.ModelAdmin):
    list_display = ('hash', 'user', 'created_at', 'edited_at')


class BannedFingerprintAdmin(admin.ModelAdmin):
    list_display = ('fingerprint', 'banned_at', 'expiry')



admin.site.register(RoomImage, RoomImageAdmin)
admin.site.register(HouseImage, HouseImageAdmin)
admin.site.register(BillFile, BillFileAdmin)
admin.site.register(PhoneNumberVerification, PhoneNumberVerificationAdmin)
admin.site.register(Fingerprint, FingerprintAdmin)
admin.site.register(BannedFingerprint, BannedFingerprintAdmin)
