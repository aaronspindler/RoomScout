from django.urls import path

from . import views

urlpatterns = [
    # Content Pages
    path('donation', views.payment_donation, name='payment_donation'),
]
