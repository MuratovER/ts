from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sphere_of_life, Profile, Post, Comment
from django.forms import ModelForm      


class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=100, help_text='Last Name')
    #last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    password2 = None

    class Meta:
        model = User
        fields = ('username','email', 'password1')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

#This form for upload ico
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class Sphere_of_life_Form(forms.ModelForm):
    class Meta:
        model = Sphere_of_life
        fields = ('inside_world', 'career', 'health', 'relationships',)

        INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 11)]
        inside_world = forms.IntegerField(label="Внутренний мир", widget=forms.Select(choices=INTEGER_CHOICES))
        career = forms.IntegerField(label="Учеба\Карьера", widget=forms.Select(choices=INTEGER_CHOICES))
        health = forms.IntegerField(label="Здоровье", widget=forms.Select(choices=INTEGER_CHOICES))
        relationships = forms.IntegerField(label="Отношения", widget=forms.Select(choices=INTEGER_CHOICES))


class PhotoForm(ModelForm):
  class Meta:
      model = Profile
      fields = ('image',)

# this form for update information about user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=150, help_text='Email')
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')

    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name')

#class ProfileUpdateForm(forms.ModelForm):
    #class Meta:
       # model = Profile
       # fields = ['image']      