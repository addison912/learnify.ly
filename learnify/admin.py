from django.contrib import admin
from learnify.models import UserProfile, Courses, Reviews, Purchases, Videos

admin.site.register(UserProfile)
admin.site.register(Courses)
admin.site.register(Reviews)
admin.site.register(Purchases)
admin.site.register(Videos)
