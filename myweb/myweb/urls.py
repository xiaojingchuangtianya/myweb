"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import Login.views as login_views
from Notes import urls as note_url
from . import views as index
from show_blog import urls as show_blog

#只写url在这边,然后不写include,这样子url不会出现分支错误
#多写re表达式
"""
主分支下只有login(登录),logout(登出),register(注册),其余得写在某个名字得次级分支下
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index.index),
    path("login",login_views.login),
    path("register",login_views.register),
    path("note/",include(note_url)),
    path("blog/show_blog/",include(show_blog))
]
