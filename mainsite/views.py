from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect ,get_object_or_404
from mainsite.forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from .models import Post, Skill, UserSkill, Profile, Sphere_of_life, User_affirmation
from .models import Post, Skill, UserSkill, Profile, Sphere_of_life, Achivement, UserAchivement
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import Sphere_of_life_Form
from django.contrib.auth.decorators import login_required
from .useful_lib import WheelOfLife, get_affirmation_image
import datetime
from django.utils.timezone import make_aware
from django.http import JsonResponse
from django.template import RequestContext

#Basic views begin
#отправляет расположение разметки страницы в файл url
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


def introduction_chapter_pritch(request):
    return  render(request, 'mainsite/tree/introduction/introduction_chapter_pritch.html',)

def introduction_chapter_koliso(request):
    return  render(request, 'mainsite/tree/introduction/introduction_chapter_koliso.html',)

@login_required
def introduction_chapter_lider_task(request):
    return  render(request, 'mainsite/tree/introduction/introduction_chapter_lider_task.html',)

@login_required
def introduction_chapter_spheres_life_task(request):
    return  render(request, 'mainsite/tree/introduction/introduction_chapter_spheres_life_task.html',)

@login_required
def sphere_deletion(request):
    try:
        sphere_del = Sphere_of_life.objects.get(user=request.user)
        sphere_del.delete() 

    except Sphere_of_life.DoesNotExist:
        pass

    try:
        achivement_delete = UserAchivement.objects.get(user=request.user)
        achivement_delete.delete() 

    except UserAchivement.DoesNotExist:
        pass  

    return redirect('introduction_chapter_spheres_life')   

    

    #return  render

@login_required
def introduction_chapter_spheres_life(request):
    # checks whether sphere already exists or not. Returns true or false
    # sphere = None

    # try:       
    #     sphere = Sphere_of_life.objects.get(user=request.user)
    # except:
    #     pass

    #if sphere != None:  
    if Sphere_of_life.objects.filter(user=request.user).exists():  
        # if already exist - edit existing
        sphere = Sphere_of_life.objects.get(user=request.user)
        if request.method == "POST":
            form = Sphere_of_life_Form(request.POST, instance=sphere)
            if form.is_valid():
                sphere = form.save(commit=False)
                sphere.save()
        else:
            form = Sphere_of_life_Form(request.POST, instance=sphere)
            
            # if form.is_valid():
            #     sphere = form.save(commit=False)
            #     sphere.save()

            # else:
            #     form = Sphere_of_life_Form()

        WheelOfLife_vars = Sphere_of_life.objects.get(user=request.user)
        img = WheelOfLife.getImageSkills([WheelOfLife_vars.inside_world, WheelOfLife_vars.career, WheelOfLife_vars.health, WheelOfLife_vars.relationships  ])

        return  render(request, 'mainsite/tree/introduction/introduction_chapter_spheres_life.html', {'form': form, 'img': img})

    else:
        # if not exist - create new
        if request.method == 'POST':     
             form = Sphere_of_life_Form(request.POST)
             if form.is_valid():
                sphere = form.save(commit=False)
                sphere.user = request.user
                sphere.save()
                
                achivement = Achivement.objects.get(name="Первые шаги")
                achivement_for_user = UserAchivement(user=request.user,achivement = achivement,level=1)
                achivement_for_user.save()            

                WheelOfLife_vars = Sphere_of_life.objects.get(user=request.user)
                img = WheelOfLife.getImageSkills([WheelOfLife_vars.inside_world, WheelOfLife_vars.career, WheelOfLife_vars.health, WheelOfLife_vars.relationships])

                return render(request, 'mainsite/tree/introduction/introduction_chapter_spheres_life.html', {'form': form, 'img': img})
               
        else:
            form = Sphere_of_life_Form()

        # achivement = Achivement.objects.get(name="Test")
        # achivement_for_user = UserAchivement(user=request.user,achivement = achivement,level=21)
        # achivement_for_user.save()

        # WheelOfLife_vars = Sphere_of_life.objects.get(user=request.user)
        # img = WheelOfLife.getImageSkills([WheelOfLife_vars.inside_world, WheelOfLife_vars.career, WheelOfLife_vars.health, WheelOfLife_vars.relationships])

        return  render(request, 'mainsite/tree/introduction/introduction_chapter_spheres_life.html', {'form': form})
    


    

# First
#подключение первой главы
def first_view(request):
    return  render(request, 'mainsite/tree/first/first_chapters.html',)

def first_chapters_what_is_it(request):
    return  render(request, 'mainsite/tree/first/first_chapters_what_is_it.html',)

def first_chapters_what_is_it_task(request):
    return  render(request, 'mainsite/tree/first/first_chapters_what_is_it_task.html',)

def first_chapters_edit(request):
    return  render(request, 'mainsite/tree/first/first_chapters_edit.html',)

def first_chapters_EditTask(request):
    return  render(request, 'mainsite/tree/first/first_chapters_EditTask.html',)

def first_chapters_self_assessment(request):
    return  render(request, 'mainsite/tree/first/first_chapters_self_assessment.html',)

def first_chapters_self_assessment_list(request):
    return  render(request, 'mainsite/tree/first/first_chapters_self_assessment_list.html',)


def first_chapters_self_discipline(request):
    return  render(request, 'mainsite/tree/first/first_chapters_self_discipline.html',)

def first_chapters_self_discipline_list(request):
    return  render(request, 'mainsite/tree/first/first_chapters_self_discipline_list.html',)

def first_chapters_aims_in_life(request):
    return  render(request, 'mainsite/tree/first/first_chapters_aims_in_life.html',)

def first_chapters_aims_in_life_list(request):
    return  render(request, 'mainsite/tree/first/first_chapters_aims_in_life_list.html',)

#Second
#подключение второй главы
def second_view(request):
    return  render(request, 'mainsite/tree/second/second_chapters.html',)

def second_chapters_AimofLearning(request):
    return  render(request, 'mainsite/tree/second/second_chapters_AimofLearning.html',)

def second_chapters_ControlofTime(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ControlofTime.html',) 

def second_chapters_ControlofTimeEfficiency(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ControlofTimeEfficiency.html',)

def second_chapters_EfficientСommunications(request):
    return  render(request, 'mainsite/tree/second/second_chapters_EfficientСommunications.html',)

def second_chapters_ForeignLanguage(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ForeignLanguage.html',)

def second_chapters_Thoughts(request):
    return  render(request, 'mainsite/tree/second/second_chapters_Thoughts.html',)      

#Third
#подключение тертей главы
def third_view(request):
    return  render(request, 'mainsite/tree/third/third_chapters.html',)

def third_chapters_HealthySleep(request):
    return  render(request, 'mainsite/tree/third/third_chapters_HealthySleep.html',)   

def third_chapters_GoodNutrition(request):
    return  render(request, 'mainsite/tree/third/third_chapters_GoodNutrition.html',)   

def third_chapters_MovementandHardening(request):
    return  render(request, 'mainsite/tree/third/third_chapters_MovementandHardening.html',)   
    
def third_chapters_LadieswithStress(request):
    return  render(request, 'mainsite/tree/third/third_chapters_LadieswithStress.html',)   

#Fourth
#подключение четвертой главы
def fourth_view(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters.html',)

def fourth_chapters_AbilitytoCommunicate(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters_AbilitytoCommunicate.html',)

def fourth_chapters_Conflicts(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters_Conflicts.html',)

def fourth_chapters_RelationshipsintheFamily(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters_RelationshipsintheFamily.html',) 

def fourth_chapters_Friends(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters_Friends.html',)        


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


@login_required
def user_page(request):

    '''
    отображает на странице профиля скилы и фичи для конкретных пользователей
    '''

    user = User.objects.get(username = request.user)
    skills = UserSkill.objects.filter(user=user)

    achivements = UserAchivement.objects.filter(user = user)
    

    sphere = None
    if Sphere_of_life.objects.filter(user=request.user).exists():
        sphere = Sphere_of_life.objects.get(user=request.user)

        WheelOfLife_vars = Sphere_of_life.objects.get(user=request.user)
    
        img = WheelOfLife.getImageSkills([WheelOfLife_vars.inside_world, WheelOfLife_vars.career, WheelOfLife_vars.health, WheelOfLife_vars.relationships  ])
    else:
        img = False

    user_affirmation_path = None
    if User_affirmation.objects.filter(user=request.user).exists():
        user_obj = User_affirmation.objects.filter(user=request.user).order_by('-id')[:1][0]
        user_text = user_obj.text
        bg_id = user_obj.background_id
        user_affirmation_path = get_affirmation_image.get_image(user_obj)
    return render(request, 'mainsite/user_page.html', {'user' : user, 'skills' : skills, 'sphere' : sphere, 'img': img, 'user_affirmation_path': user_affirmation_path})




#signup view
def signup_view(request):

    '''вьюха с логикой регистрации'''

    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        #user.profile.first_name = form.cleaned_data.get('first_name')
        #user.profile.last_name = form.cleaned_data.get('last_name')
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

@login_required
def affirmation_generator(request):
    if request.method == "POST":
        print("AFFIRM TEST :::::::::::", request.POST)
        # affirmation = User_affirmation.objects.get(name="Первые шаги")
        # return  render(request, 'mainsite/affirmation_generator.html',)
        affirmation = User_affirmation(
            user=request.user,
            text = request.POST["text"],
            date_change = make_aware(datetime.datetime.now()),
            background_id = request.POST["bg_id"],
            color = request.POST["color"],
            font_type = request.POST["font-type"]
        )
        affirmation.save()


    return  render(request, 'mainsite/affirmation_generator.html',)

   # return render_to_response('fileupload/upload.html', {'form': c['UploadFileForm']},  RequestContext(request))


#
# API FUNCTIONS
#
from django.http import JsonResponse
from .serializers import TodoListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET']) # Декоратор для красивого браузерного вывода
def api_get_todolist(request):
    # Как пример показан вывод сфер жизни по api запросу
    # Позже будет прикручен to-do лист
    if request.method == "GET":
        user_request = request.GET.get('user_id')
        if not user_request.isdigit():
            return JsonResponse({"error": "parameter error"})
        spheres = Sphere_of_life.objects.filter(user = user_request) if Sphere_of_life.objects.filter(user = user_request).exists() else False
        if not spheres:
            return JsonResponse({"error": "not exist"})
        serializer = TodoListSerializer(spheres, many = True)
        return Response(serializer.data)