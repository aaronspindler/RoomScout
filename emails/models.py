from django.db import models


class EmailMessage(models.Model):

	sent_at = models.DateTimeField(auto_now_add=True)
	
	from_email = models.EmailField()
	to_email = models.EmailField()
	subject = models.TextField()
	text_content = models.TextField()
	html_content = models.TextField()