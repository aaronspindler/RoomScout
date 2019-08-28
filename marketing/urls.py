from django.urls import path

from . import views

urlpatterns = [
	path('roommates', views.marketing_roommates, name='marketing_roommates'),
]
