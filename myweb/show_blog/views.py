from django.shortcuts import render,HttpResponse
from content.models import Blog
# Create your views here.


# 展示首页,name为接受url的参数
def show_class(request,class_name):
    if class_name=="首页":
        print("这是首页！")
        return render(request,"首页.html")
    if class_name=="个人信息":
        return HttpResponse("信息处理")
    class_blog=Blog.objects.filter(classification=class_name)
    return render(request,"home_page.html",context={"blogs":class_blog})

# 这里展示博客详情
def show_blog_detail(request,title):
    print(title)
    blog_detail=Blog.objects.filter(title=title)
    return HttpResponse(blog_detail[0].text)