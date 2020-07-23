from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout
from Login.models import User_pro

#设置为首页,如果还没有登录就显示登录页面,已经登录显示用户操作界面
def index(request):
    # if request.user.is_authenticated:
    try:
        pro_mes=User_pro.objects.filter(id=request.user.id)[0]
    except:
        pro_mes=None
    return render(request,"index.html",context={"pro_mes":pro_mes})
    # else:
    #     return HttpResponse("你尚未登陆<a href='/login'>前往登录</a>")

