from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#为用户添加额外的信息
class User_pro(models.Model):
    ToUser=models.OneToOneField(User,on_delete=models.CASCADE)#一对一,级联删除
    Head_icon=models.ImageField(upload_to="head_icon",blank=True)#头像地址
    Birthday=models.DateField(blank=True)#生日
    Site=models.CharField(blank=True,max_length=100)#住址