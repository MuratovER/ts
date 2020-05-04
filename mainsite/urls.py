from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from . import views
from django.shortcuts import render






urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path(r'^signup/$', views.signup, name='signup'),
    path('', views.user_page, name='user_page'),
    
    
]