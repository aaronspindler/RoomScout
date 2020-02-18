from django.contrib import admin

from security.models import Fingerprint, BannedFingerprint, IP


class IPAdmin(admin.ModelAdmin):
    list_display = ('address', 'user', 'created_at')


class FingerprintAdmin(admin.ModelAdmin):
    list_display = ('hash', 'user', 'ip', 'created_at')


class BannedFingerprintAdmin(admin.ModelAdmin):
    list_display = ('fingerprint', 'banned_at', 'expiry')


admin.site.register(IP, IPAdmin)
admin.site.register(Fingerprint, FingerprintAdmin)
admin.site.register(BannedFingerprint, BannedFingerprintAdmin)
