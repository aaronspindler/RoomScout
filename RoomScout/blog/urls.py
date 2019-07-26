from django.urls import path

from . import views

urlpatterns = [
	path('', views.blogs, name='blog_home'),
]
