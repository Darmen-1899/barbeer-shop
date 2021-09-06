import services as services
from django.db import models


# Create your models here.

class Service(models.Model):
    serviceName = models.TextField(max_length=150)
    img = models.ImageField(max_length=150)
    price = models.TextField(max_length=150)

    def __str__(self):
        return self.serviceName

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Booking(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    service = models.CharField(max_length=150,null=True)
    name = models.TextField(null=True)
    email = models.EmailField(null=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
