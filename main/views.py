from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Service, Booking
from thebarbeer import settings


def index(request):
    service = Service.objects.all()[:10]
    return render(request, 'index.html', {'service': service})


def create_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        time = request.POST['time']
        select = request.POST['service']
        email = request.POST['email']
        Booking.objects.create(date=date, time=time, service=select, name=name, email=email)
        # Booking.save()
        # a = Booking.objects.create(date=request.POST["date"],time=request.POST["time"],services=request.POST["select"],name=request.POST["name"],
        #                            email=request.POST["email"])
        if email:
            subject = 'Запись на ' + select
            message = name + ' , спасибо за запись на ' + select + '. Дата : ' + date + ' время ' + time + '.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
    return render(request, "index.html")


