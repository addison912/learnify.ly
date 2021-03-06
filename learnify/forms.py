from django import forms
from learnify.models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('profile_pic', 'first_name', 'last_name')


class CourseForm(forms.ModelForm):

    class Meta():
        model = Course
        fields = ('title', 'category', 'price', 'description',
                'preview_video', 'course_image' ,'video_format')


class VideoForm(forms.ModelForm):

    class Meta():
        model = Video
        fields = ('title', 'description', 'video', 'video_format',  'lesson_number',)

class ReviewForm(forms.ModelForm):

    class Meta():
        model = Review
        fields = ('title', 'body')

