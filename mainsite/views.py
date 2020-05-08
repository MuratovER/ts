from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mainsite.forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext





def home_page(request):
    return render(request, 'mainsite/home.html',)
 #   return render(request, 'blog/user_page.html',)


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home_page')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})
'''
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            
            return redirect('home')
    else:
        form = SignUpForm()
        
    return render(request, 'registratio/nsignup.html', {'form': form})
'''