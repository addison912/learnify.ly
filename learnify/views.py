from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from learnify.forms import *
from learnify.models import *
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe

logged_in_user = None
stripe.api_key = settings.SECRET


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
        {"profile": profile, "logged_in_user": logged_in_user, "purchases": purchases},
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
def checkout(request, pk):
    global logged_in_user
    new_purchase = Purchase(
        course = Course.objects.get(id=pk),
        purchaser = logged_in_user
    )
    print('HERE IS THE TYPE')
    print(type(new_purchase.course.price))
    print( round(new_purchase.course.price, 2))

    if request.method == "POST":
        token = request.POST.get("stripeToken")

    try:
        charge = stripe.Charge.create(
            amount= int(new_purchase.course.price),
            currency='usd',
            description=Course.title,
            source=request.POST['stripeToken']
        )

        new_purchase.charge_id = charge.id
    
    except stripe.error.CardError as ce:
        return False, ce

    else:
        new_purchase.save()
        return render(request, 'learnify/charge.html')