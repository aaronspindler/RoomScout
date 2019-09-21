from django.contrib import admin

from .models import IP, RoomImage, HouseImage, BillFile, PhoneNumberVerification

admin.site.register(IP)
admin.site.register(RoomImage)
admin.site.register(HouseImage)
admin.site.register(BillFile)
admin.site.register(PhoneNumberVerification)
