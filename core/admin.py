from django.contrib import admin
from .models import CustomUser,Resume,Job,Application,JobMatch

@admin.register(CustomUser)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','username','email','first_name','last_name']
    

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['title','id']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['title','id']


@admin.register(Application)
class JobAdmin(admin.ModelAdmin):
    list_display=['id']

@admin.register(JobMatch)
class JobAdmin(admin.ModelAdmin):
    list_display=['id']

