from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from accounts.views import SignUp, login

urlpatterns = [
    path('', views.home, name='home'),
    # Auth
    path('signup', SignUp.as_view() ,name='signup'),
    path('login', LoginView.as_view() ,name='login'),
    path('logout', LogoutView.as_view() ,name='logout'),
]
