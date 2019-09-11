from django.urls import path

from . import views

urlpatterns = [
	path('find/', views.room_list, name='room_list'),
	path('search/', views.room_search, name='room_search'),
	path('search/', views.room_search_results, name='room_search_results'),
	path('create/', views.room_create, name='room_create'),
	path('<str:pk>/detail/', views.room_detail.as_view(), name='room_detail'),
	path('<str:pk>/edit/', views.room_edit.as_view(), name='room_edit'),
	path('<str:pk>/delete/', views.room_delete.as_view(), name='room_delete'),
	path('<str:pk>/addphoto/', views.room_add_photo, name='room_add_photo'),
]
