from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from accounts.views import signup, login, settings

urlpatterns = [
    path('', views.home, name='home'),

    # Accounts
    path('signup', signup ,name='signup'),
    path('settings', settings ,name='settings'),
    path('login', LoginView.as_view() ,name='login'),
    path('logout', LogoutView.as_view() ,name='logout'),
    #Houses
    path('house/', include('houses.urls')),
    #Rooms
    path('room/', include('rooms.urls')),
    #Management
    path('manager/', include('management.urls'))
]
