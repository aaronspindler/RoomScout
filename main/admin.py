from django.contrib import admin

from .models import ContactMessage, BugReport

admin.site.register(ContactMessage)
admin.site.register(BugReport)