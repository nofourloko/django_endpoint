from django.contrib import admin
from django.urls import path, include
from .views import EndpointApiView

urlpatterns = [
    path('api', EndpointApiView.as_view()),
]