from django.contrib import admin
from .models import CustomUser,Resume

@admin.register(CustomUser)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','username','email','first_name','last_name']
    

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['title']