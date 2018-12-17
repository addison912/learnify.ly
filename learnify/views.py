from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from learnify.forms import *
from learnify.models import *


def index(request):
    return render(request, 'learnify/index.html')


def courses(request):
    courses = Course.objects.all()
    return render(request, 'learnify/courses.html', {'courses': courses})


def course_detail(request):
    course = Course.objects.get(id=pk)
    return render(request, 'learnify/course_detail.html', {'course': course})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'learnify/create_course_form.html', {'form': form})


def profile(request):
    return render(request, 'learnify/profile.html')


def about(request):
    return render(request, 'learnify/about.html')
