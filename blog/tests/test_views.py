import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from blog.models import BlogPost


class BlogViewsTests(TestCase):
	def setUp(self):
		self.client = Client()
		User = get_user_model()
		self.user = User.objects.create_user(username='FredFlintstone', email='fred@flintstone.com', password='babadoo')
	
	def test_blog_views_BlogListView_empty(self):
		print('Testing blog.views.BlogListView GET empty')
		response = self.client.get(reverse('blog_home'), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/blog.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertContains(response, 'It looks like there are no posts right now, come back soon!')
	
	def test_blog_views_BlogListView_filled(self):
		print('Testing blog.views.BlogListView GET filled')
		blog_post = BlogPost.objects.create(title='Fancy Blog Post', pub_date=datetime.datetime.now(), body='This is a fancy blog post!')
		response = self.client.get(reverse('blog_home'), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/blog.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertNotContains(response, 'It looks like there are no posts right now, come back soon!')
		self.assertContains(response, 'Fancy Blog Post')
	
	def test_blog_views_BlogDetailView(self):
		print('Testing blog.views.BlogListView GET filled')
		blog_post = BlogPost.objects.create(title='Fancy Blog Post', pub_date=datetime.datetime.now(), body='This is a fancy blog post!')
		response = self.client.get(reverse('blog_post', kwargs={'pk': blog_post.id}), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/blog_post.html')
		self.assertNotContains(response, '404')
		self.assertNotContains(response, 'Login')
		self.assertNotContains(response, 'It looks like there are no posts right now, come back soon!')
		self.assertContains(response, 'Fancy Blog Post')