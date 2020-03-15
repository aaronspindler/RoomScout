from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'supportus', 'contactus', 'blog_home', 'licenses', 'privacypolicy', 'termsofuse', 'account_signup', 'account_login', 'billfeatures', 'verificationfeatures']

    def location(self, item):
        return reverse(item)
