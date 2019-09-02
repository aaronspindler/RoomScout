from django.urls import path

from . import views

urlpatterns = [
	path('<str:pk>/delete/', views.bill_delete, name='bill_delete'),
]
