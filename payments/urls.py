from django.urls import path

from . import views

urlpatterns = [
    # Content Pages
    path('charge', views.payment_charge, name='payment_charge'),
]
