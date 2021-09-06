from django.conf.urls import url, include
from django.contrib import admin
from main import views
from django.urls import path


app_name = 'main'
urlpatterns = [
    url(r'^main/', views.index, name='main'),
    path("", views.index, name='index'),
    path("create_book/", views.create_book, name="create_book")
]
