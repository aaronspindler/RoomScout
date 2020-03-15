from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView

from blog.sitemaps import BlogSitemap
from houses.sitemaps import HouseSitemap
from main.sitemaps import StaticSitemap
from rooms.sitemaps import RoomSitemap

sitemaps = {
    'static': StaticSitemap,
    'blog': BlogSitemap,
    'houses': HouseSitemap,
    'rooms': RoomSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots/robots.txt", content_type='text/plain')),
    path('', include('main.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler403 = 'main.views.permission_denied'
handler404 = 'main.views.page_not_found'
handler500 = 'main.views.server_error'

admin.site.site_header = "Roomscout Admin"
admin.site.site_title = "Roomscout Admin Portal"
admin.site.index_title = "Welcome to Roomscout Admin Portal"
