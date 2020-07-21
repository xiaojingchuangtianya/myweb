from django.urls import path,re_path
from . import views

urlpatterns=[
    # 匹配2-10个中英文字符,这样所有想都匹配这个函数处理了
   path("name=<str:name>",views.show_home),
    path("title=<str:title>",views.show_blog)
]