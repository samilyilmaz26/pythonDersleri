from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User" , on_delete=models.CASCADE, verbose_name = "Yazar Adı")
    title = models.CharField(max_length=50 ,verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now=True, verbose_name="Yaratılma Tarihi")
    image_field = models.FileField(blank=True, null= True , verbose_name="Makale Fotoğrafı")
    def __str__(self):
        return self.title  