from django.contrib.sitemaps import Sitemap
from .models import House

class HouseSitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return House.objects.all()