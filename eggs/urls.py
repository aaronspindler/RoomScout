from django.urls import path

from . import views

urlpatterns = [
    path('dog', views.dog, name='ee_dog'),
]
