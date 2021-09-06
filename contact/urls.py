from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from .views import FeedBackView


app_name = 'contact'
urlpatterns = [
    url('^$', views.contact),
    path(r'leave_feedback', views.leave_feedback , name='leave_feedback'),
]