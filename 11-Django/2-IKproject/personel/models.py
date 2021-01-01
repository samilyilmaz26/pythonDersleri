from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=50 ,verbose_name="Başlık")
    description = RichTextField()
    def __str__(self):
        return self.name
class Personel(models.Model):
    cityid = models.ForeignKey("cities" , on_delete=models.CASCADE, verbose_name = "Şehir Kodu")
    name = models.CharField(max_length=50 ,verbose_name="Ad")
    surname  = models.CharField(max_length=50 ,verbose_name="Soyad ")
    salary = models.FloatField(verbose_name="Maaş")
    birthdate = models.DateField(verbose_name= "Doğum Yılı ")
    def __str__(self):
        return self.name