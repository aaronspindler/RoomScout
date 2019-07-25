from django.urls import path

from . import views

urlpatterns = [
	path('create/', views.house_create, name='house_create'),
	path('<str:pk>/detail/', views.house_detail.as_view(), name='house_detail'),
	path('<str:pk>/edit/', views.house_edit.as_view(), name='house_edit'),
	path('<str:pk>/delete/', views.house_delete.as_view(), name='house_delete'),
]
