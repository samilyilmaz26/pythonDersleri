from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from . forms import LoginForm,RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def  loginuser (request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    } 
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username =username ,password =password) 
        if user is  None:
            messages.warning(request,"Yanlış Kullanıcı veya şifre ")
            return render(request,"login.html" ,  context= context)
        messages.success(request,"Giriş Başarılı")
        login(request,user)
        return redirect("index")
    return render(request,"login.html" , context= context)
def  logoutuser (request):
    logout(request)
    messages.success(request,"Çıkış İşlemi Başarılı ....")
    return  redirect ("index")
def  register (request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newuser = User(username = username)
        newuser.set_password(password)
        newuser.save()
        login(request,newuser)
        messages.success(request, "Kullanıcı Başarı ile yaratıldı")
        return redirect("index")
    context = {
    "form": form
    }
    return render(request , "register.html" , context= context)
 