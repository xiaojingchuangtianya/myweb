from django.urls import path,re_path
from . import views

urlpatterns=[
    # 匹配2-10个中英文字符,这样所有想都匹配这个函数处理了
    re_path(r"([\u4e00-\u9fa5_a-zA-Z0-9_]{2,10})",views.show_home),
]