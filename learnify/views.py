from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from learnify.forms import *
from django.conf import settings
from django.views.generic.base import TemplateView


# class CoursesPageView(TemplateView):
#     template_name = 'courses.html'

#     def get_context_data(self, **kwargs): # new
#         context = super().get_context_data(**kwargs)
#         context['key'] = settings.STRIPE_PUBLISHABLE_KEY
#         return context


def index(request):
    return render(request, 'learnify/index.html')


def courses(request):
    courses = Course.objects.all()
    stripe_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'learnify/courses.html', {'courses': courses, 'stripe_key': stripe_key})


def course_detail(request):
    course = Course.objects.get(id=pk)
    return render(request, 'learnify/course_detail.html', {'course': course})


def profile(request):
    return render(request, 'learnify/profile.html')


def about(request):
    return render(request, 'learnify/about.html')
