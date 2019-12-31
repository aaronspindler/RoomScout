from django.contrib import admin

from .models import Room, Inquiry, RoomLike


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'house', 'price', 'is_available', 'created_at', 'updated_at')


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'status')


class RoomLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'room')


admin.site.register(Room, RoomAdmin)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(RoomLike, RoomLikeAdmin)
