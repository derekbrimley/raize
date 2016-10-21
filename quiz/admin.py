from django.contrib import admin

# Register your models here.
from .models import MyUser, Response, UserScore, AlumniScores, MajorScores, UserMajors

admin.site.register(MyUser)
admin.site.register(Response)
admin.site.register(UserScore)
admin.site.register(AlumniScores)
admin.site.register(MajorScores)
admin.site.register(UserMajors)