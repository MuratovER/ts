from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mainsite.forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from .models import Post, Skill, UserSkill, Profile, Sphere_of_life
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import Sphere_of_life_Form
from django.contrib.auth.decorators import login_required

from .useful_lib import WheelOfLife


#Basic views begin

def home_page(request):
    return render(request, 'mainsite/home.html',)

@login_required
def achivement_view(request):
    return render(request, 'mainsite/achivements.html',)

@login_required
def to_do_list_view(request):
    return render(request, 'mainsite/to_do_list.html',)

@login_required
def blog_view(request):
    return render(request, 'mainsite/blog.html',)

@login_required
def tree_view(request):
    return render(request, 'mainsite/tree.html', )

@login_required
def help_view(request):
    return render(request, 'mainsite/help.html',)

@login_required
def skills(request):
    return render(request, 'mainsite/skills.html',)

@login_required
def introduction_view(request):
    return  render(request, 'mainsite/tree/introduction/introduction_chapters.html',)

@login_required
def introduction_chapter_lider(request):
    return  render(request, 'mainsite/tree/introduction/introduction_chapter_lider.html',)

@login_required
def introduction_chapter_spheres_life(request):
    # checks whether sphere already exists or not. Returns true or false
    if Sphere_of_life.objects.filter(user=request.user).exists():
        # if already exist - edit existing
        sphere = Sphere_of_life.objects.get(user=request.user)
        if request.method == "POST":
            form = Sphere_of_life_Form(request.POST, instance=sphere)
            if form.is_valid():
                sphere = form.save(commit=False)
                sphere.save()
        else:
            form = Sphere_of_life_Form()
        WheelOfLife_vars = Sphere_of_life.objects.get(user=request.user)
        img = WheelOfLife.getImageSkills([WheelOfLife_vars.inside_world, WheelOfLife_vars.career, WheelOfLife_vars.health, WheelOfLife_vars.relationships  ])

        return  render(request, 'mainsite/tree/introduction/introduction_chapter_spheres_life.html', {'form': form, 'path': img})
    else:
        # if not exist - create new
        if request.method == "POST":
            form = Sphere_of_life_Form(request.POST)
            if form.is_valid():
                sphere = form.save(commit=False)
                sphere.user = request.user
                sphere.save()
        else:
            form = Sphere_of_life_Form()

        # WheelOfLife_vars = Sphere_of_life.objects.get(user=request.user)
        # img = WheelOfLife.getImageSkills([WheelOfLife_vars.inside_world, WheelOfLife_vars.career, WheelOfLife_vars.health, WheelOfLife_vars.relationships  ])

        return  render(request, 'mainsite/tree/introduction/introduction_chapter_spheres_life.html', {'form': form})
    
    
@login_required
def introduction_chapter_lider_task(request):
    return  render(request, 'mainsite/tree/introduction/introduction_chapter_lider_task.html',)

@login_required
def introduction_chapter_spheres_life_task(request):
    return  render(request, 'mainsite/tree/introduction/introduction_chapter_spheres_life_task.html',)

def first_view(request):
    return  render(request, 'mainsite/tree/first/first_chapters.html',)

def first_chapters_what_is_it(request):
    return  render(request, 'mainsite/tree/first/first_chapters_what_is_it.html',)

def first_chapters_edit(request):
    return  render(request, 'mainsite/tree/first/first_chapters_edit.html',)

def first_chapters_self_assessment(request):
    return  render(request, 'mainsite/tree/first/first_chapters_self_assessment.html',)

def first_chapters_self_discipline(request):
    return  render(request, 'mainsite/tree/first/first_chapters_self_discipline.html',)

def first_chapters_aims_in_life(request):
    return  render(request, 'mainsite/tree/first/first_chapters_aims_in_life.html',)

#Basic views end

#blog view begin
@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mainsite/blog.html', {'posts': posts})

@login_required
def skills(request):
    skills = Skill.objects.all()
    return render(request, 'mainsite/skills.html', {'skills': skills})



#blog view end
# def user_page(request, username):
#     user = User.objects.get(username=username)
#     skills = UserSkill.objects.filter(user=user)
#     return render(request, 'mainsite/user_page.html', {'user' : user, 'skills' : skills})

@login_required
def user_page(request):
    user = User.objects.get(username = request.user)
    skills = UserSkill.objects.filter(user=user)

    sphere = None
    if Sphere_of_life.objects.filter(user=request.user).exists():
        sphere = Sphere_of_life.objects.get(user=request.user)

        WheelOfLife_vars = Sphere_of_life.objects.get(user=request.user)
    
        img = WheelOfLife.getImageSkills([WheelOfLife_vars.inside_world, WheelOfLife_vars.career, WheelOfLife_vars.health, WheelOfLife_vars.relationships  ])
    else:
        img = False
    return render(request, 'mainsite/user_page.html', {'user' : user, 'skills' : skills, 'sphere' : sphere, 'path': img})


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

