from django.contrib import admin

from security.models import Fingerprint, BannedFingerprint


class FingerprintAdmin(admin.ModelAdmin):
    list_display = ('hash', 'user', 'created_at', 'edited_at')


class BannedFingerprintAdmin(admin.ModelAdmin):
    list_display = ('fingerprint', 'banned_at', 'expiry')


admin.site.register(Fingerprint, FingerprintAdmin)
admin.site.register(BannedFingerprint, BannedFingerprintAdmin)