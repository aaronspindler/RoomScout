from django.urls import path

from . import views

urlpatterns = [
    path('<str:pk>/delete/', views.bill_delete, name='bill_delete'),
    path('<str:pk>/addfile/', views.bill_add_file, name='bill_add_file'),
]
