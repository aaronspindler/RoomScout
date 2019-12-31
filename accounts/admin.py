from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'general_contact', 'promo_contact', 'is_premium_member', 'max_houses')


admin.site.register(User, UserAdmin)
