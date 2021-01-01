from django.shortcuts import render, get_object_or_404,redirect
from . models import Cities,Personel
from . forms import CitiesForm,PersonelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user import views
from datetime import datetime


# Create your views here.
def  index (request):
    return  render(request, "index.html")
def  about (request):
    return  render(request, "about.html")
def  cities (request):
    cities = Cities.objects.all()
    return  render(request, "cities/cities.html" , {"cities" : cities })
def  citydetail (request,id):
    #city = Cities.objects.filter(id = id).first
    city =  get_object_or_404(Cities,id= id )
    return  render(request, "cities/citydetail.html" ,{"city": city}) 
@login_required(login_url="user:loginuser"  )
def  cityadd (request):
    form = CitiesForm(request.POST or None)
    if form.is_valid():
        form.save()
        #city.save()
        messages.success(request, "Şehir Başarı ile kayıt edildi")
        return redirect("cities")
    return  render(request, "cities/cityadd.html",  {"form" :form})
@login_required(login_url="user:loginuser"  )
def citydelete(request, id ):
    city = get_object_or_404(Cities , id =id )
    city.delete()
    messages.success(request, "Şehir Başarı ile Silindi")
    return redirect("cities")
@login_required(login_url="user:loginuser"  )
def cityedit(request, id ):
    city = get_object_or_404(Cities , id =id   )
    form = CitiesForm(request.POST or None ,instance= city)
    if form.is_valid():
        city = form.save()
        city.save()
        messages.success(request, "Şehir Başarı ile Güncellendi")
        return redirect("cities")
    return render(request, "cities/cityedit.html" ,{"form": form})
def  personels (request):
    personels = Personel.objects.all()
    return  render(request, "personel/personels.html" , {"personels" : personels })
def  personeladd (request):
    form = PersonelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Personel  Başarı ile kayıt edildi")
        return redirect("personels")
    return  render(request, "personel/personelsingle.html",  {"form" :form})
@login_required(login_url="user:loginuser"  )
def personeledit(request, id ):
    personel = get_object_or_404(Personel , id =id   )
    form = PersonelForm(request.POST or None ,instance= personel)
    birthdate =  personel.birthdate.strftime("%m/%d/%Y")
    print(birthdate)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y" )
    print("date and time:",date_time)	 
    if form.is_valid():
        personel = form.save()
        personel.save()
        messages.success(request, "personel Başarı ile Güncellendi")
        return redirect("personels")
    return render(request, "personel/personelsingle.html" ,{"form": form  ,"birthdate": birthdate}  )