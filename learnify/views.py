from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from learnify.forms import *
from learnify.models import *
from django.conf import settings

logged_in_user = None


def index(request):
    registered = False
    global logged_in_user
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
            registered = True
            return redirect("user_login")
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # global logged_in_user
        user_form = UserForm()
        profile_form = UserProfileForm()
        # profile = logged_in_user
    return render(
        request,
        "learnify/index.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
            "logged_in_user": logged_in_user,
        },
    )


def courses(request):
    courses = Course.objects.all()
    stripe_key = settings.APIKEY
    return render(
        request,
        "learnify/courses.html",
        {
            "courses": courses,
            "stripe_key": stripe_key,
            "logged_in_user": logged_in_user,
        },
    )
    return render(request, 'learnify/courses.html', {
        'courses': courses,
        'stripe_key': stripe_key,
    })


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    return render(
        request,
        "learnify/course_detail.html",
        {"course": course, "logged_in_user": logged_in_user},
    )
    price = Course.objects.get(price)
    return render(request, 'learnify/course_detail.html', {'course': course}, {'price': price})


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            global logged_in_user
            course = form.save(commit=False)
            course.owner_id = logged_in_user.pk
            if "preview_video" in request.FILES:
                course.preview_video = request.FILES["preview_video"]
            course.save()
            return redirect("course_detail", pk=course.pk)
    else:
        form = CourseForm()
    return render(
        request,
        "learnify/create_course_form.html",
        {"form": form, "logged_in_user": logged_in_user},
    )


def profile(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user)
    global logged_in_user
    logged_in_user = profile
    purchases = Purchase.objects.filter(purchaser=profile)
    return render(
        request,
        "learnify/profile.html",
<<<<<<< HEAD
        {"profile": profile, "logged_in_user": logged_in_user, "purchases": purchases},
=======
        {"profile": profile, "logged_in_user": logged_in_user, "purchases":purchases},
>>>>>>> 7310e1ff0701ccea0a57b5a9de87b502f5b857a5
    )

def about(request):
    return render(request, "learnify/about.html", {"logged_in_user": logged_in_user})


@login_required
def special(request):
    return HttpResponse("You are logged in")


@login_required
def user_logout(request):
    logout(request)
    return redirect("index")


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
            registered = True
            return redirect("user_login")
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(
        request,
        "learnify/index.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
        },
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(f"profile/{username}")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f"They used username: {username} and password {password}")
            return HttpResponse("Invalid login details given")
    else:
        return render(request, "learnify/login.html", {})

@login_required
def payment(request):
    user = User.objects.get(id=request.user.id)
    purchases = Purchase.objects.filter(purchaser=profile, purchases=course)
    content = {
        "stripe_key": settings.STRIPE_TEST_PUBLIC_KEY,
        "purchases": purchases,
    }
    return render(request, "learnify/", content)
