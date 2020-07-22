from django.shortcuts import render
from content.models import Blog
# Create your views here.
# 展示首页,name为接受url的参数
def show_home(request,name):
    class_blog=Blog.objects.filter(classification=name)
    return render(request,"home_page.html",context={"blogs":class_blog})