from django.urls import path
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
]
