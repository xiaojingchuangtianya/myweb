from django.shortcuts import render,HttpResponse
from content.models import Blog
# Create your views here.


# 展示首页,name为接受url的参数
def show_home(request,name):
    print(name)
    class_blog=Blog.objects.filter(classification=name)#根据博客类名来获取博客的内容
    return render(request,"home_page.html",context={"blogs":class_blog})

# 需要先写处理函数，返回内容
def show_blog(request,title):
    print("获取博客"+title)
    blog_detail=Blog.objects.filter(title=title)
    return render(request,"blog_detail.html",context={"title":title,"detail":blog_detail})