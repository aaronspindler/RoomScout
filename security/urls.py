from django.urls import path

from . import views

urlpatterns = [
    path('fingerprint/save/', views.fingerprint_save, name='security_fingerprint_save'),
]
