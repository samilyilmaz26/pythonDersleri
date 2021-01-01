from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=500, verbose_name="Adı")
    surname = models.CharField(max_length=500, verbose_name="Soyadı")
    no = models.IntegerField(verbose_name="Numarası")

    class Meta:
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'

    def __str__(self):
        return self.name
