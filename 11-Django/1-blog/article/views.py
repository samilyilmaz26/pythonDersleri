from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from . forms import ArticleForm 
from . models import Article
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def  index (request):
    return  render(request, "index.html")
def  about (request):
    return  render(request, "about.html")
def articles (request):
    articles = Article.objects.all()
    return render(request , "articles.html" , {"articles" :articles})
@login_required(login_url="user:login"  )
def myarticles (request):
    articles = Article.objects.filter(author = request.user)
    return  render(request , "myarticles.html", {"articles" :articles} )
def detail (request, id):
    #article = Article.objects.filter(id = id).first
    article = get_object_or_404(Article, id =id)
    return render(request , "detail.html" , {"article": article})
@login_required(login_url="user:login"  )
def update(request, id ):
    article = get_object_or_404(Article , id =id   )
    form = ArticleForm(request.POST or None ,instance= article)
    if form.is_valid():
        article = form.save(commit= False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Başarı ile Güncellendi")
        return redirect("article:myarticles")
    return render(request, "update.html" ,{"form": form})
@login_required(login_url="user:login"  )
def delete(request, id ):
    article = get_object_or_404(Article , id =id )
    article.delete()
    messages.success(request, "Makale Başarı ile Silindi")
    return redirect("article:myarticles")
@login_required(login_url="user:login" )
def add(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit= False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Başarı ile kayıt edildi")
        return redirect("article:myarticles")
    return render(request, "add.html" ,{"form": form})