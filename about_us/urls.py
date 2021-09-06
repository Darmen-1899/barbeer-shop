from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url('^$', views.index),
    path('about', views.index, name='about'),

]