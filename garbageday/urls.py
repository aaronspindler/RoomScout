from django.urls import path

from . import views

urlpatterns = [
	path('manage/', views.garbageday_manage, name='garbageday_manage'),
	path('create/', views.garbageday_create, name='garbageday_create'),
	path('edit/', views.garbageday_edit, name='garbageday_edit'),
	path('delete/', views.garbadgeday_delete, name='garbageday_delete'),
]
