from django.contrib.sitemaps import Sitemap

from .models import BlogPost


class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return BlogPost.objects.all()
