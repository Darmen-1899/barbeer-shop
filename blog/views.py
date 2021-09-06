from django.shortcuts import render

# Create your views here.
from blog.models import New


def index(request):
    news_list = New.objects.all()[:5]
    return render(request, 'blog.html', {'news_list': news_list})
