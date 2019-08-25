from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
	def items(self):
		return ['home', 'about', 'contactus', 'licenses', 'privacypolicy', 'termsofuse', 'account_signup', 'account_login']

	def location(self, item):
		return reverse(item)