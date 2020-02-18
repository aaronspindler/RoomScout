from django.db import models
from security.models import IP


class ContactMessage(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	sender = models.EmailField(default='')
	subject = models.TextField(default='')
	message = models.TextField(default='')
	ip = models.ForeignKey(IP, on_delete=models.DO_NOTHING, blank=True, null=True)

	def __str__(self):
		return "{} - {} - {}".format(self.created_at, self.sender, self.subject)
