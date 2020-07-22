from django.shortcuts import render,HttpResponse


#设置为首页,如果还没有登录就显示登录页面,已经登录显示用户操作界面
def index(request):
    if request.user.is_authenticated:
        return render(request,"index.html")
    else:
        return HttpResponse("你尚未登陆<a href='/login'>前往登录</a>")
