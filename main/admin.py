from django.contrib import admin

from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'sender', 'subject', 'ip')


admin.site.register(ContactMessage, ContactMessageAdmin)
