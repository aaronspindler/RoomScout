from django.contrib import admin

from .models import User, PhoneNumberVerification

admin.site.register(User)
admin.site.register(PhoneNumberVerification)
