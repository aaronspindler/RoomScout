from . import views
from django.urls import path

urlpatterns = [
	path('', views.blogs, name='blog_home'),
]
