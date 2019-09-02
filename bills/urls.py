from django.urls import path

from . import views

urlpatterns = [
	path('<str:pk>/add/', views.bill_add, name='bill_add'),
]
