from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.room_create ,name='room_create'),
    path('detail/<str:pk>/', views.room_detail.as_view() ,name='room_detail'),
    path('edit/<str:pk>/', views.room_edit.as_view() ,name='room_edit'),
    path('delete/<str:pk>/', views.room_delete.as_view() ,name='room_delete'),
]
