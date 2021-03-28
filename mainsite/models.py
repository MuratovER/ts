from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm
from cloudinary.models import CloudinaryField



#an extended version of the posts that help you make the post)
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.IntegerField(default='0')
    views = models.IntegerField(default='0')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

# created comments for your articles
class Comment(models.Model):
    post = models.ForeignKey('mainsite.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

#difficulty logic with level and reavrd tabs
class Difficulty(models.Model):
    '''
    System of dificulty for all other models
    Таблица системы сложностей с ячейками уровня и награды
    '''
    level = models.CharField(max_length=20)
    reward = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.level


class Skill(models.Model):
    '''
        Skill logic with changable difficulty description ico an name
        Таблицы для скилов с ячеками названия скила описания иконки и сложности
    '''
    skill_name = models.TextField()
    skill_description = models.TextField()
    skill_ico = models.ImageField(upload_to='img')#form of ico image located in forms.py
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, related_name="difficulty", null=True)
    def __str__(self):
        return self.skill_name


#model of userSKill
class UserSkill(models.Model): 
    '''
    Таблица в которой отображаются скилы присвоенные юзеру со своей сложностью
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="skill", default=0)
    level = models.PositiveIntegerField(default=0)


#model for Profile
class Profile(models.Model):
    '''
    таблица профиля с именем фамилией почтой и краткой биографией
    а также полем image куда пользователь загружает свой аватар
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150, null=True)
    bio = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Sphere_of_life(models.Model):
    '''
    таблица для фичи колеса жизни с возможностью выбора в каждой сфере от 1 до 10
    '''
    INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 11)]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inside_world = models.IntegerField(verbose_name="Внутренний мир", choices=INTEGER_CHOICES)
    career = models.IntegerField(verbose_name="Учеба\Карьера", choices=INTEGER_CHOICES)
    health = models.IntegerField(verbose_name="Здоровье", choices=INTEGER_CHOICES)
    relationships = models.IntegerField(verbose_name="Отношения", choices=INTEGER_CHOICES)
    def __str__(self):
        return self.user.username


class User_affirmation(models.Model):
    """
    Пользовательские аффирмации.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank = True, null = True)
    date_change = models.DateTimeField(blank = True, null = True)
    background_id = models.PositiveSmallIntegerField(blank = True, null = True)
    color = models.CharField(max_length=6, blank=True, null=True)
    font_type = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'Пользовательские аффирмации'
        verbose_name = 'Аффирмация'
        ordering = ['-user']








class Achivement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, related_name="achiv_difficulty", null=True) 
    def __str__(self):
        return self.name 


class UserAchivement(models.Model): 
    '''
    Таблица в которой отображаются достижения присвоенные юзеру со своей сложностью
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    achivement = models.ForeignKey(Achivement, on_delete=models.CASCADE, related_name="achivement", default=0)
    level = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.achivement.name



