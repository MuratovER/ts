from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth import views
from . import views
from django.shortcuts import render
from django.conf.urls import include, url





urlpatterns = [
    path('', views.home_page, name='home_page'),
    
    path('signup/', views.signup_view, name='signup'),
    path('user_page/', views.user_page, name='user_page'), 
    path('achivements/', views.achivement_view, name='achivements'),
    path('to_do_list/', views.to_do_list_view, name='to_do_list'),
    path('blog/', views.blog_view, name='blog'),
    path('messages/', views.messages_view, name='messages'),
    path('help/', views.help_view, name='help'),
    
  
    
]