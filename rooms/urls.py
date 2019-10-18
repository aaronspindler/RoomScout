from django.urls import path

from . import views

urlpatterns = [
	path('find/', views.room_list, name='room_list'),
	path('create/', views.room_create, name='room_create'),
	path('saved/', views.room_saved, name="room_saved"),
	path('<str:pk>/detail/', views.room_detail.as_view(), name='room_detail'),
	path('<str:pk>/edit/', views.room_edit.as_view(), name='room_edit'),
	path('<str:pk>/delete/', views.room_delete.as_view(), name='room_delete'),
	path('<str:pk>/addphoto/', views.room_add_photo, name='room_add_photo'),
	path('<str:pk>/deletephoto/', views.room_delete_photo, name='room_delete_photo'),
	path('<str:pk>/inquire/', views.room_inquire, name='room_inquire'),
	path('<str:pk>/inquire/dismiss', views.room_inquire_dismiss, name='room_inquire_dismiss'),
]
