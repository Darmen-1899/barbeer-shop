from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.views.generic import ListView, DeleteView
from blog.models import New

app_name = "blog"
urlpatterns = [
    url('^$', views.index, name='news_list'),
]