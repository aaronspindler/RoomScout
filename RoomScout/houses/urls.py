from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.house_create ,name='house_create'),
    path('detail/<str:pk>/', views.house_detail.as_view() ,name='house_detail'),
    path('edit/<str:pk>/', views.house_edit.as_view() ,name='house_edit'),
    path('delete/<str:pk>/', views.house_delete.as_view() ,name='house_delete'),
]
