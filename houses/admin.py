from django.contrib import admin

from .models import House, Invitation


class HouseAdmin(admin.ModelAdmin):
    list_display = ('full_address', 'user', 'lat', 'lon')


class InvitationAdmin(admin.ModelAdmin):
    list_display = ('house', 'target', 'sender')


admin.site.register(House, HouseAdmin)
admin.site.register(Invitation, InvitationAdmin)
