from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField




# Create your models here.
class Blog(models.Model):
    chooices=(
        ("home","主页"),
        ("crawl","爬虫"),
        ("Algorithmic","算法"),
        ("html","前端"),
        ("Django","Django"),
        ("school","大学"),
        ("travel","旅游"),
        ("pets","宠物"),
        ("lover","爱情")
    )
    classification=models.CharField(max_length=50,choices=chooices)#分类
    title=models.CharField(max_length=50)#标题
    text=RichTextField(verbose_name="博客内容")#博客主体内容
    author=models.ForeignKey(User,on_delete=models.CASCADE)#作者,外键连接到User,级联删除
    create_time=models.DateTimeField(auto_now_add=True)#在新建时直接被创建,无法在添加时手动添加修改
    def __str__(self):
        return self.title

    # 排序方式,由创建时间从近到远
    class Meta:
        ordering=["-create_time"]