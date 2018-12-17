from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from learnify.forms import *


def index(request):
    return render(request, 'learnify/index.html')


def courses(request):
    courses = Course.objects.all()
    return render(request, 'learnify/courses.html', {'courses': courses})


def course_detail(request):
    course = Course.objects.get(id=pk)
    return render(request, 'learnify/course_detail.html', {'course': course})


def profile(request):
    return render(request, 'learnify/profile.html')


def about(request):
    return render(request, 'learnify/about.html')

@login_required
def special(request):
    return HttpResponse('You are logged in')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'learnify/registratiion.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse('Your account was inactive.')
        else:
            print('Someone tried to login and failed.')
            print(f'They used username: {username} and password {password}')
            return HttpResponse('Invalid login details given')
    else:
        return render(request, 'learnify/login.html', {})