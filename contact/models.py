from django.db import models

# Create your models here.

class Contact(models.Model):
    message = models.TextField()
    firstname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

