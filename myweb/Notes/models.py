from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    #外键一对一连接User
    user=models.OneToOneField(to=User,on_delete=models.DO_NOTHING)
    notes=models.TextField()
    delete=models.BooleanField(blank=True,default=False)#默认未删除,不允许为空