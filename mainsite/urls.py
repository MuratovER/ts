from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth import views
from . import views
from django.shortcuts import render
from django.conf.urls import include, url
from mainsite.views import user_page



# path('user_page/', views.user_page, name='user_page'),
#адреса которые ссылаются на вьюхи
urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('accounts/login/', views.LoginView.as_view(), name='login'),
	path('signup/', views.signup_view, name='signup'),
	path('user_page/<slug:username>/', views.user_page, name='user_page'),
	path('achivements/', views.achivement_view, name='achivements'),
	path('to_do_list/', views.to_do_list_view, name='to_do_list'),
	path('profile_settings/', views.profile_settings, name='profile_settings'),
	path('blog/', views.post_list, name='post_list'),
	path('blog/drafts/', views.post_draft_list, name='post_draft_list'),
	path('blog/article/new/', views.post_new, name='post_new'),
	path('blog/article/<int:pk>/', views.post_detail, name='post_detail'),
	path('blog/article/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('blog/article/<pk>/publish/', views.post_publish, name='post_publish'),
	path('blog/article/<pk>/remove/', views.post_remove, name='post_remove'),
	path('blog/article/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	path('blog/article/<int:pk>/like/', views.add_post_like, name='add_post_like'),
	path('blog/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('blog/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

	path('tree/', views.tree_view, name='tree'),
	path('tree_old/', views.tree_old, name='tree_old'),
	path('help/', views.help_view, name='help'),
	path('skills/', views.skills, name='skills'),
	path('aboutus/', views.aboutus, name='aboutus'),
	#Introduction
	path('introduction/', views.introduction_view, name='introduction'),
	path('introduction/introduction_chapter_lider/', views.introduction_chapter_lider, name='introduction_chapter_lider'),
	path('introduction/introduction_chapter_pritch/', views.introduction_chapter_pritch, name='introduction_chapter_pritch'),
	path('introduction/introduction_chapter_koliso/', views.introduction_chapter_koliso, name='introduction_chapter_koliso'),
	path('introduction/introduction_chapter_spheres_life/', views.introduction_chapter_spheres_life, name='introduction_chapter_spheres_life'),
	path('introduction/introduction_chapter_lider_task/', views.introduction_chapter_lider_task, name='introduction_chapter_lider_task'),
	path('introduction/introduction_chapter_spheres_life_task/', views.introduction_chapter_spheres_life_task, name='introduction_chapter_spheres_life_task'),
	#First
	path('first/', views.first_view, name='first'),
	path('first/first_chapters_what_is_it/', views.first_chapters_what_is_it, name='first_chapters_what_is_it'),
	path('first/first_chapters_what_is_it_task/', views.first_chapters_what_is_it_task, name='first_chapters_what_is_it_task'),
	path('first/first_chapters_edit/', views.first_chapters_edit, name='first_chapters_edit'),
	path('first/first_chapters_EditTask/', views.first_chapters_EditTask, name='first_chapters_EditTask'),
	path('first/first_chapters_self_assessment/', views.first_chapters_self_assessment, name='first_chapters_self_assessment'),
	path('first/first_chapters_self_assessment_list/', views. first_chapters_self_assessment_list, name='first_chapters_self_assessment_list'),
	path('first/first_chapters_self_discipline/', views.first_chapters_self_discipline, name='first_chapters_self_discipline'),
	path('first/first_chapters_self_discipline_list/', views.first_chapters_self_discipline_list, name='first_chapters_self_discipline_list'),
	path('first/first_chapters_aims_in_life/', views.first_chapters_aims_in_life, name='first_chapters_aims_in_life'),
	path('first/first_chapters_self_aims_in_life_list/', views.first_chapters_self_aims_in_life_list, name='first_chapters_self_aims_in_life_list'),
	#Second
	path('second/', views.second_view, name='second'),
	path('second/second_chapters_AimofLearning/', views.second_chapters_AimofLearning, name='second_chapters_AimofLearning'),
	path('second/second_chapters_AimofLearning_task/', views.second_chapters_AimofLearning_task, name='second_chapters_AimofLearning_task'),
	path('second/second_chapters_ControlofTime/', views.second_chapters_ControlofTime, name='second_chapters_ControlofTime'),
	path('second/second_chapters_ControlofTime_task/', views.second_chapters_ControlofTime_task, name='second_chapters_ControlofTime_task'),
	path('second/second_chapters_ControlofTimeEfficiency/', views.second_chapters_ControlofTimeEfficiency, name='second_chapters_ControlofTimeEfficiency'),
	path('second/second_chapters_ControlofTimeEfficiency_task/', views.second_chapters_ControlofTimeEfficiency_task, name='second_chapters_ControlofTimeEfficiency_task'),
	path('second/second_chapters_EfficientСommunications/', views.second_chapters_EfficientСommunications, name='second_chapters_EfficientСommunications'),
	path('second/second_chapters_EfficientСommunications_task/', views.second_chapters_EfficientСommunications_task, name='second_chapters_EfficientСommunications_task'),
	path('second/second_chapters_ForeignLanguage/', views.second_chapters_ForeignLanguage, name='second_chapters_ForeignLanguage'),
	path('second/second_chapters_ForeignLanguage_task/', views.second_chapters_ForeignLanguage_task, name='second_chapters_ForeignLanguage_task'),
	path('second/second_chapters_Thoughts/', views.second_chapters_Thoughts, name='second_chapters_Thoughts'),
	path('second/second_chapters_Thoughts_task/', views.second_chapters_Thoughts_task, name='second_chapters_Thoughts_task'),
	#Third
	path('third/', views.third_view, name='third'),
	path('third/third_chapters_HealthySleep/', views.third_chapters_HealthySleep, name='third_chapters_HealthySleep'),
	path('third/third_chapters_GoodNutrition/', views.third_chapters_GoodNutrition, name='third_chapters_GoodNutrition'),
	path('third/third_chapters_MovementandHardening/', views.third_chapters_MovementandHardening, name='third_chapters_MovementandHardening'),
	path('third/third_chapters_LadieswithStress/', views.third_chapters_LadieswithStress, name='third_chapters_LadieswithStress'),
	path('third/third_chapters_HealthySleep_task/', views.third_chapters_HealthySleep_task, name='third_chapters_HealthySleep_task'),
	path('third/third_chapters_GoodNutrition_task/', views.third_chapters_GoodNutrition_task, name='third_chapters_GoodNutrition_task'),
	path('third/third_chapters_MovementandHardening_task/', views.third_chapters_MovementandHardening_task, name='third_chapters_MovementandHardening_task'),
	path('third/third_chapters_LadieswithStress_task/', views.third_chapters_LadieswithStress_task, name='third_chapters_LadieswithStress_task'),
	#Fourth
	path('fourth/', views.fourth_view, name='fourth'),
	path('fourth/fourth_chapters_AbilitytoCommunicate/', views.fourth_chapters_AbilitytoCommunicate, name='fourth_chapters_AbilitytoCommunicate'),
	path('fourth/fourth_chapters_Conflicts/', views.fourth_chapters_Conflicts, name='fourth_chapters_Conflicts'),
	path('fourth/fourth_chapters_RelationshipsintheFamily/', views.fourth_chapters_RelationshipsintheFamily, name='fourth_chapters_RelationshipsintheFamily'),
	path('fourth/fourth_chapters_Friends/', views.fourth_chapters_Friends, name='fourth_chapters_Friends'),
	path("affirmation_generator", views.affirmation_generator, name='affirmation_generator'),
	path('fourth/fourth_chapters_AbilitytoCommunicate_task/', views.fourth_chapters_AbilitytoCommunicate_task, name='fourth_chapters_AbilitytoCommunicate_task'),
	path('fourth/fourth_chapters_Conflicts_task/', views.fourth_chapters_Conflicts_task, name='fourth_chapters_Conflicts_task'),
	path('fourth/fourth_chapters_RelationshipsintheFamily_task/', views.fourth_chapters_RelationshipsintheFamily_task, name='fourth_chapters_RelationshipsintheFamily_task'),
	path('fourth/fourth_chapters_Friends_task/', views.fourth_chapters_Friends_task, name='fourth_chapters_Friends_task'),
	#End
	path('end/', views.end_view, name='end'),
	#API
	#re_path(r'^api/get_todolist/(?P<user_id>[\w.@+-]+)/$', views.api_get_todolist),
	path('api/get_todolist/', views.api_get_todolist),
	path('introduction/introduction_chapter_spheres_life/delete/', views.sphere_deletion, name='sphere_deletion'),
	path('user_page/image_upload/', views.profile_image_upload, name='profile_image_upload'),
	# path('blog/new_blog_categories', views.new_blog_categories, name='new_blog_categories'),
	path('blog/new_blog', views.new_blog, name='new_blog')

]