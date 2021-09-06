from django.contrib import admin

# Register your models here.
from main.models import Service, Booking

admin.site.register(Service)
admin.site.register(Booking)


