from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.room_create ,name='room_create'),
    path('detail/<int:key>/', views.room_detail.as_view() ,name='room_detail'),
    path('edit/<int:key>/', views.room_edit.as_view() ,name='room_edit'),
    path('delete/<int:key>/', views.room_delete.as_view() ,name='room_delete'),
]
