from django.urls import path

from . import views

urlpatterns = [
    path('manage/<str:house>/', views.garbageday_manage, name='garbageday_manage'),
    path('create/<str:house>/', views.garbageday_create, name='garbageday_create'),
    path('edit/<str:house>/', views.garbageday_edit, name='garbageday_edit'),
]
