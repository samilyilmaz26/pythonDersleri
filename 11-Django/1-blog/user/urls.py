from django.contrib import admin
from django.urls import path
from . import views
app_name = "user" 

urlpatterns = [
    path('loginuser/', views.loginuser , name="login"), 
    path('logoutuser/', views.logoutuser , name="logout"), 
    path('register/', views.register , name="register"), 
]