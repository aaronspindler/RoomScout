from django.urls import path, include

from accounts.views import settings, preferences
from . import views

urlpatterns = [
	# Content Pages
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('contactus', views.contactus, name='contactus'),
	path('licenses', views.licenses, name='licenses'),
	path('privacypolicy', views.privacypolicy, name='privacypolicy'),
	path('termsofuse', views.termsofuse, name='termsofuse'),
	path('changes', views.changelog, name='changelog'),
	path('dashboard', include('dashboard.urls')),
	path('sandbox', views.sandbox, name='sandbox'),

	# Blog
	path('blog/', include('blog.urls')),

	# Accounts
	path('accounts/', include('allauth.urls')),
	path('settings', settings, name='settings'),
	path('settings/preferences', preferences, name='settings_preferences'),

	# Bills
	path('bill/', include('bills.urls')),

	# Houses
	path('house/', include('houses.urls')),
	# Rooms
	path('room/', include('rooms.urls')),
	# Marketing
	path('m/', include('marketing.urls')),
]
