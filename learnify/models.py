from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Courses(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    isFeatured = models.BooleanField(default=False)
    date_created = models.DateField(
        auto_now=True, auto_now_add=False, editable=False)
    date_updated = models.DateField(auto_now=False, auto_now_add=True)
    owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='course')
    preview_video = models.FileField(upload_to='course_videos', blank=True)

    def __str__(self):
        return self.title


class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='course_videos', blank=True)
    description = models.TextField(blank=True)
    order_number = models.IntegerField()
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.title


class Reviews(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.title


class Purchases(models.Model):
    course = models.ForeignKey(
        Courses, on_delete=models.DO_NOTHING, related_name='purchases')
    purchaser = models.ForeignKey(
        UserProfile, on_delete=models.DO_NOTHING, related_name='purchases')

    def __str__(self):
        return self.course.title
