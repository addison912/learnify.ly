from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('courses/<int:pk>', views.course_detail, name='course_detail'),
    path('profile', views.profile, name='profile'),
    path('user_login', views.user_login, name='user_login'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    # path('api/users', views.sendJson, name='sendJson'),
    path('special', views.special, name='special')
]
