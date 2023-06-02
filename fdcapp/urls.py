from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('cloudform/', views.cloud_request.as_view(), name='cloudform')
]
