from django.shortcuts import render


#设置为首页,如果还没有登录就显示登录页面,已经登录显示用户操作界面
def index(request):
    return render(request,"index.html")
