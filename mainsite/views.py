from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mainsite.forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from .models import Post, Skill, UserSkill, Profile
from django.utils import timezone



#Basic views begin

def home_page(request):
    return render(request, 'mainsite/home.html',)
 #   return render(request, 'blog/user_page.html',)

def user_page(request):
    return render(request, 'mainsite/user_page.html',)

def achivement_view(request):
    return render(request, 'mainsite/achivements.html',)

def to_do_list_view(request):
    return render(request, 'mainsite/to_do_list.html',)

def blog_view(request):
    return render(request, 'mainsite/blog.html',)

def messages_view(request):
    return render(request, 'mainsite/messages.html',)

def help_view(request):
    return render(request, 'mainsite/help.html',)



#Basic views end



#blog view begin
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mainsite/blog.html', {'posts': posts})

#blog view end



def skill_list(request):
    skills = Post.objects.order_by('skill_name')
    return render(request, 'mainsite/user_page.html', {'skills': skills})



def get_user_profile(request, username):
    user = User.objects.get(username=username)
    skills = UserSkill.objects.filter(user=user)
    return render(request, 'mainsite/user_page.html', {"user":user})








#signup view
def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('user_page')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})  
 