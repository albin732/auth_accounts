from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserDetailModel

# Register your models here.



class AdmUserDetail(admin.ModelAdmin):
    list_display = ('user','user_type','contact_number')






admin.site.register(UserDetailModel,AdmUserDetail)