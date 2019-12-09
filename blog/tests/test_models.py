from django.test import TestCase
import datetime
from blog.models import BlogPost


class BlogModelTests(TestCase):
	def test_BlogPost_creation(self):
		print('Testing blog.models.BlogPost creation')
		pre_count = BlogPost.objects.count()
		blog_post = BlogPost.objects.create(title='Fancy Blog Post', pub_date=datetime.datetime.now(), body='This is a fancy blog post!')
		post_count = BlogPost.objects.count()
		self.assertGreater(post_count, pre_count)