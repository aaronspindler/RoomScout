from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.management_home, name='management_home'),
]
