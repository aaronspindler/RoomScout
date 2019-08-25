from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from main.sitemaps import StaticSitemap
from blog.sitemaps import BlogSitemap
from houses.sitemaps import HouseSitemap
from rooms.sitemaps import RoomSitemap

sitemaps = {
	'static': StaticSitemap,
	'blog': BlogSitemap,
	'houses': HouseSitemap,
	'rooms': RoomSitemap,
}

urlpatterns = [
	path('admin/', admin.site.urls),
	path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('', include('main.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
