from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#为用户添加额外的信息
class User_pro(models.Model):
    to_user=models.OneToOneField(User,on_delete=models.CASCADE)#一对一,级联删除
    head_icon=models.ImageField(upload_to="head_icon",blank=True)#头像地址
    birthday=models.DateField(blank=True)#生日
    site=models.CharField(blank=True,max_length=100)#住址