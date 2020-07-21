from django.urls import path
from . import views as note_views

urlpatterns=[
    path("index_json",note_views.index_json),
    path("index",note_views.index),
]