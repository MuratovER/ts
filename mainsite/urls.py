from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.user_page, name='user_page'),
    
]