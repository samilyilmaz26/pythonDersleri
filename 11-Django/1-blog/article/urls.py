from django.contrib import admin
from django.urls import path
from . import views
app_name = "article" 

urlpatterns = [
    path('articles/', views.articles, name="articles"), 
    path('myarticles/', views.myarticles, name="myarticles"), 
    path('detail/<int:id>', views.detail, name="detail"), 
    path('update/<int:id>', views.update, name="update"), 
    path('delete/<int:id>', views.delete, name="delete"), 
    path('add' , views.add, name="add"), 
]