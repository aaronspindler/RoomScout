from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts.views import settings
from . import views

urlpatterns = [
	# Content Pages
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('contactus', views.contactus, name='contactus'),
	path('licenses', views.licenses, name='licenses'),
	path('privacypolicy', views.privacypolicy, name='privacypolicy'),
	path('termsofuse', views.termsofuse, name='termsofuse'),

	# Blog
	path('blog/', include('blog.urls')),

	# Accounts
	path('accounts/', include('allauth.urls')),
	path('settings', settings, name='settings'),
	#path('logout', LogoutView.as_view(), name='logout'),
	# Houses
	path('house/', include('houses.urls')),
	# Rooms
	path('room/', include('rooms.urls')),
	# Management
	path('manager/', include('management.urls'))
]
