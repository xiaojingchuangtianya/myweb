from django.urls import path,re_path
from . import views

urlpatterns=[
    path("class=<str:class_name>",views.show_class),
    path("title=<str:title>",views.show_blog_detail)
]