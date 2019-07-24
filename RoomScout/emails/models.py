from django.db import models


class Email(models.Model):
	sent_at = models.DateTimeField(auto_now_add=True)
	sent_to = models.EmailField()
	subject = models.TextField()
	contents = models.TextField()
