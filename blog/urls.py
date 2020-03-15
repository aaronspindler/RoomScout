from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_home'),
    path('<str:pk>/', views.BlogDetailView.as_view(), name='blog_post'),
]
