from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField()

	def get_absolute_url(self):
		return reverse('blog_post', args=[str(self.id)])