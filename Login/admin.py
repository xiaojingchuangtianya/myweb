from django.contrib import admin
from .models import User_pro
from django.contrib.auth.admin import UserAdmin as BaseUseradmin
from django.contrib.auth.models import User
# Register your models here.
class Profile(admin.StackedInline):
    model = User_pro
    can_delete = False
    verbose_name = "用户信息补充"

#将用户身份pro注册到用户user内
class UserAdmin(BaseUseradmin):
    inlines = [Profile,]

#重新注册UserAdmin
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
