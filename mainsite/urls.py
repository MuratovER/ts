from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from . import views
from django.shortcuts import render
from django.conf.urls import include, url





urlpatterns = [
   
 
    path('signup/', views.signup_view, name='signup'),
    path('', views.home_page, name='home_page'),
   
    
]