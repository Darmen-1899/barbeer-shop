from django.db import models


# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Стаья"
        verbose_name_plural = "Статьи"
