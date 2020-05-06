from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from . import views
from django.shortcuts import render
from django.conf.urls import include, url





urlpatterns = [
   
 
    path(r'^signup/$', views.signup_view, name='signup'),
    path('', views.user_page, name='user_page'),
    
    
]