from django.contrib import admin

from .models import Room, Inquiry, RoomLike

admin.site.register(Room)
admin.site.register(Inquiry)
admin.site.register(RoomLike)
