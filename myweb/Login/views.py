from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import RegForm,LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.
def my_login(request):
    form=LoginForm()
    if request.method=="POST":
        # 获取账号密码
        username=request.POST["account"]
        password=request.POST["password"]
        #将来再设置验证码功能
        user=authenticate(username=username,password=password)
        print(user)
        # 如果登录为真实有效,返回主页
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html",context={"form":form,"error":"yes"})
    return render(request,"login.html",context={"form":form})


def register(request):
    forms=RegForm()
    if request.method =="post":
        #这里写一个存储注册信息的,然后有信息重合,注册错漏等问题会回退到这边继续
        return redirect("/")  # 注册完后直接跳转首页
    return render(request, "register.html", context={"form": RegForm})
# 退出
def web_logout(request):
    logout(request)
    return redirect("/")










