from django.contrib import admin

from .models import EmailMessage


class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('sent_at', 'subject', 'from_email', 'to_email')


admin.site.register(EmailMessage, EmailMessageAdmin)
