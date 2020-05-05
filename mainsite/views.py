from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mainsite.forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView


def user_page(request):
    return render(request, 'mainsite/base.html',)
 #   return render(request, 'blog/user_page.html',)




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
        
    return render(request, 'registration/signup.html', {'form': form})