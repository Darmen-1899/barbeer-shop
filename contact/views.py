from django.shortcuts import render, redirect
from .forms import FeedBackForm
# Create your views here.
from contact.models import Contact
from django.views.generic import View


def contact(request):
    return render(request, 'contact.html')


def leave_feedback(request):
    a = Contact.objects.create(firstname=request.POST['firstname'], email=request.POST['email'],
                               subject=request.POST['subject'], message=request.POST['message'])
    return render(request, 'contact.html')


class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
