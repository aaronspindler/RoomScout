from django.db import models


class ContactMessage(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	sender = models.EmailField(default='')
	subject = models.TextField(default='')
	message = models.TextField(default='')
	ip = models.GenericIPAddressField()


class BugReport(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	sender = models.EmailField(default='')
	subject = models.TextField(default='')
	message = models.TextField(default='')
	ip = models.GenericIPAddressField()
