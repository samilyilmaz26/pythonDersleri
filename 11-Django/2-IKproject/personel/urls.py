from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "personel"

urlpatterns = [
    path('cities', views.cities, name="cities"),
    path('cityadd', views.cityadd, name="cityadd"),
    path('citydetail/<int:id>', views.citydetail, name="citydetail"),
    path('citydelete/<int:id>', views.citydelete , name="citydelete"),
    path('cityedit/<int:id>', views.cityedit , name="cityedit"),
    path('personels/', views.personels, name="personels"),
    path('personeladd/',views.personeladd , name="personeladd"),
    path('personeledit/<int:id>',views.personeledit , name="personeledit"),
]
