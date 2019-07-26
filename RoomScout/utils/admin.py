from django.contrib import admin

from .models import IP, Email, PublicImage, RoomImage, PrivateFile

admin.site.register(IP)
admin.site.register(Email)
admin.site.register(PublicImage)
admin.site.register(RoomImage)
admin.site.register(PrivateFile)