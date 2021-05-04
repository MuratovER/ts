from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect ,get_object_or_404
from mainsite.forms import SignUpForm, PhotoForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from .models import Post, Skill, UserSkill, Profile, Sphere_of_life, Achivement, UserAchivement, User_affirmation, Comment 
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import Sphere_of_life_Form, PostForm, CommentForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .useful_lib import WheelOfLife, get_affirmation_image
import datetime
from django.shortcuts import redirect
from django.utils.timezone import make_aware
from django.http import JsonResponse
from django.template import RequestContext
from cloudinary.forms import cl_init_js_callbacks      
from django.http import HttpResponseRedirect
from django.http import HttpResponse


#Basic views begin
#отправляет расположение разметки страницы в файл url

# if user authenticated load home, else load landing page
def home_page(request): 
    #print(request.user)
    if request.user.is_authenticated:
        return render(request, 'mainsite/home.html',)
    else:
        if request.user_agent.is_mobile:
            return render(request, 'mainsite/mobile/landing.html',)
        else:    
            return render(request, 'mainsite/landing.html',)

 
    

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
def tree_old(request):
    return render(request, 'mainsite/tree_old.html', )

@login_required
def help_view(request):
    return render(request, 'mainsite/help.html',)

@login_required
def skills(request):
    return render(request, 'mainsite/skills.html',)
    
def aboutus(request):
    return render(request, 'mainsite/aboutus.html',)    

def aboutus(request):
    return render(request, 'mainsite/aboutus.html',)

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
    user_affirmation_path = None
    if User_affirmation.objects.filter(user=request.user).exists():
        user_obj = User_affirmation.objects.filter(user=request.user).order_by('-id')[:1][0]
        user_text = user_obj.text
        bg_id = user_obj.background_id
        user_affirmation_path = get_affirmation_image.get_image(user_obj)
    return  render(request, 'mainsite/tree/first/first_chapters_edit.html', {'user_affirmation_path': user_affirmation_path})

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

def first_chapters_self_aims_in_life_list(request):
    return  render(request, 'mainsite/tree/first/first_chapters_self_aim_in_life_list.html',)

#Second
#подключение второй главы
def second_view(request):
    return  render(request, 'mainsite/tree/second/second_chapters.html',)

def second_chapters_AimofLearning(request):
    return  render(request, 'mainsite/tree/second/second_chapters_AimofLearning.html',)

def second_chapters_AimofLearning_task(request):
    return  render(request, 'mainsite/tree/second/second_chapters_AimofLearning_task.html',)

def second_chapters_ControlofTime(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ControlofTime.html',) 

def second_chapters_ControlofTime_task(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ControlofTime_task.html',)

def second_chapters_ControlofTimeEfficiency(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ControlofTimeEfficiency.html',)

def second_chapters_ControlofTimeEfficiency_task(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ControlofTimeEfficiency_task.html',)

def second_chapters_EfficientСommunications(request):
    return  render(request, 'mainsite/tree/second/second_chapters_EfficientСommunications.html',)

def second_chapters_EfficientСommunications_task(request):
    return  render(request, 'mainsite/tree/second/second_chapters_EfficientСommunications_task.html',)

def second_chapters_ForeignLanguage(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ForeignLanguage.html',)

def second_chapters_ForeignLanguage_task(request):
    return  render(request, 'mainsite/tree/second/second_chapters_ForeignLanguage_task.html',)

def second_chapters_Thoughts(request):
    return  render(request, 'mainsite/tree/second/second_chapters_Thoughts.html',)      

def second_chapters_Thoughts_task(request):
    return  render(request, 'mainsite/tree/second/second_chapters_Thoughts_task.html',)

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

def third_chapters_HealthySleep_task(request):
    return  render(request, 'mainsite/tree/third/third_chapters_HealthySleep_task.html',)

def third_chapters_GoodNutrition_task(request):
    return  render(request, 'mainsite/tree/third/third_chapters_GoodNutrition_task.html',)

def third_chapters_MovementandHardening_task(request):
    return  render(request, 'mainsite/tree/third/third_chapters_MovementandHardening_task.html',)

def third_chapters_LadieswithStress_task(request):
    return  render(request, 'mainsite/tree/third/third_chapters_LadieswithStress_task.html',)

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

def fourth_chapters_AbilitytoCommunicate_task(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters_AbilitytoCommunicate_task.html',)

def fourth_chapters_Conflicts_task(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters_Conflicts_task.html',)

def fourth_chapters_RelationshipsintheFamily_task(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters_RelationshipsintheFamily_task.html',)

def fourth_chapters_Friends_task(request):
    return  render(request, 'mainsite/tree/fourth/fourth_chapters_Friends_task.html',)

def end_view(request):
    return  render(request, 'mainsite/tree/end/end_chapter.html',)


#Basic views end

#blog view begin
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mainsite/post_edit.html', {'form': form})

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mainsite/post_list.html', {'posts': posts})

@login_required
def post_list_my(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mainsite/post_list_my.html', {'posts': posts})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'mainsite/post_draft_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    profile = Profile.objects.get(user=request.user)
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'mainsite/post_detail.html', {'post': post, 'profile': profile})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('post_detail', pk=post.pk)
    return render(request, 'mainsite/post_edit.html', {'form': form})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_list')

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'mainsite/add_comment_to_post.html', {'form': form, 'post': post, 'profile': profile})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_list')

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_list')

@login_required
def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    response = HttpResponse()
    if request.COOKIES.get(f'{pk}') != None:
        return redirect('post_list')

    else:
        if post.user_likes == False:
            post.likes += 1
            response.set_cookie(f'{pk}', 'liked')
            post.save()
            return response
        else:
            return redirect('post_list')

@login_required
def skills(request):
    skills = Skill.objects.all()
    return render(request, 'mainsite/skills.html', {'skills': skills})

@login_required
def new_blog(request):
    return render(request, 'mainsite/blogs/blogs_creator.html', )
#blog view end


def profile_image_upload(request):
    '''
        Функция с загрузкой изображения в облочное хранилище cloudinary и привязкой к пользователю
    '''
    context = dict(backend_form = PhotoForm())
    if request.method == 'POST':
        # form = PhotoForm(request.POST, request.FILES)
        #context = {'form': form}
        user = Profile.objects.get(user = request.user)
        form = PhotoForm(request.POST, request.FILES, instance=user)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
        return redirect('user_page')
            
    return render(request, 'mainsite/image_upload.html', context)



@login_required
def user_page(request):


    '''
    отображает на странице профиля скилы и фичи для конкретных пользователей
    '''

    user = User.objects.get(username = request.user)
    
    profile = Profile.objects.get(user= request.user)
    
    skills = UserSkill.objects.filter(user=user)
    
    #profile_picture = user.i 

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
    return render(request, 'mainsite/user_page.html', 
                            {
                                'user' : user, 
                                'skills' : skills, 
                                'sphere' : sphere, 
                                'img' : img, 
                                'user_affirmation_path' : user_affirmation_path,
                                'profile': profile,
                                
                            })




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

# views for update info about user
@login_required
def profile_settings(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
       # p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid(): #and p_form.is_valid():
            u_form.save()
            #p_form.save()
            #messages.success(request, f"Your info has been changed!")
            return redirect('profile_settings')    
    else:
        u_form = UserUpdateForm(instance=request.user)
       # p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
   
    context = {
        'u_form': u_form,
        #'p_form': p_form
    }
    return render(request, 'registration/profile_settings.html', context)

