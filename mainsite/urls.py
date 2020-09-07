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
    path('blog/', views.post_list, name='blog'),
    path('tree/', views.tree_view, name='tree'),
    path('help/', views.help_view, name='help'),
    path('skills/', views.skills, name='skills'),
    path('introduction/', views.introduction_view, name='introduction'),
    path('introduction/introduction_chapter_lider/', views.introduction_chapter_lider, name='introduction_chapter_lider'),
    path('introduction/introduction_chapter_spheres_life/', views.introduction_chapter_spheres_life, name='introduction_chapter_spheres_life'),
    path('introduction/introduction_chapter_lider_task/', views.introduction_chapter_lider_task, name='introduction_chapter_lider_task'),
    path('introduction/introduction_chapter_spheres_life_task/', views.introduction_chapter_spheres_life_task, name='introduction_chapter_spheres_life_task'),
    path('first/', views.first_view, name='first'),
    path('first/first_chapters_what_is_it/', views.first_chapters_what_is_it, name='first_chapters_what_is_it'),
    path('first/first_chapters_edit/', views.first_chapters_edit, name='first_chapters_edit'),
    path('first/first_chapters_self_assessment/', views.first_chapters_self_assessment, name='first_chapters_self_assessment'),
    path('first/first_chapters_self_discipline/', views.first_chapters_self_discipline, name='first_chapters_self_discipline'),
    path('firstr/first_chapters_aims_in_life/', views.first_chapters_aims_in_life, name='first_chapters_aims_in_life'),
]