from django.urls import path

from . import views

urlpatterns = [
	path('create/', views.house_create, name='house_create'),
	path('list/', views.house_list, name='house_list'),
	path('<str:pk>/detail/', views.house_detail, name='house_detail'),
	path('<str:pk>/rooms/add/', views.house_add_room, name='house_add_room'),
	path('<str:pk>/edit/', views.house_edit.as_view(), name='house_edit'),
	path('<str:pk>/delete/', views.house_delete.as_view(), name='house_delete'),
]
