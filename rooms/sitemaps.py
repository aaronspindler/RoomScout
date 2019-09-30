from django.contrib.sitemaps import Sitemap

from .models import Room


class RoomSitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return Room.objects.all()
