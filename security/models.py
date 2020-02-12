from django.db import models

from accounts.models import User


class Fingerprint(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	edited_at = models.DateTimeField(auto_now=True)
	hash = models.TextField()
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)


class BannedFingerprint(models.Model):
	banned_at = models.DateTimeField(auto_now_add=True)
	edited_at = models.DateTimeField(auto_now=True)
	fingerprint = models.ForeignKey(Fingerprint, on_delete=models.CASCADE)
	expiry = models.DateTimeField(blank=True, null=True)
