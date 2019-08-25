from django.urls import path

from . import views

urlpatterns = [
	path('create/', views.house_create, name='house_create'),
	path('<str:pk>/detail/', views.house_detail, name='house_detail'),
	path('<str:pk>/rooms/add/', views.house_add_room, name='house_add_room'),
	path('<str:pk>/edit/', views.house_edit.as_view(), name='house_edit'),
	path('<str:pk>/delete/', views.house_delete.as_view(), name='house_delete'),
	path('<str:pk>/invite/', views.house_invite, name='house_invite'),
	path('<str:pk>/invite/remove/<str:id>/', views.house_invite_remove, name='house_invite_remove'),
	path('<str:pk>/invite/accept/<str:id>/', views.house_invite_accept, name='house_invite_accept'),
	path('<str:pk>/invite/decline/<str:id>/', views.house_invite_decline, name='house_invite_decline'),
	path('<str:pk>/member/remove/<str:id>/', views.house_member_remove, name='house_member_remove'),
]
