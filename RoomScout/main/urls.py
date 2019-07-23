from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from accounts.views import signup, login, settings

urlpatterns = [
    #Content Pages
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contactus'),
    path('licenses', views.licenses, name='licenses'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('termsandconditons', views.termsandconditons, name='termsandconditons'),

    # Accounts
    path('signup', signup ,name='signup'),
    path('settings', settings ,name='settings'),
    path('login', login ,name='login'),
    path('logout', LogoutView.as_view() ,name='logout'),
    #Houses
    path('house/', include('houses.urls')),
    #Rooms
    path('room/', include('rooms.urls')),
    #Management
    path('manager/', include('management.urls'))
]
