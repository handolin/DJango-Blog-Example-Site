from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404
import requests
from .models import Article

# Create your views here.
# localhost: http://127.0.0.1:8000/


def index(request):
    articles = Article.objects.all().order_by('-id')[:4]

    context = {
        'articles': articles

    }
    return render(request, 'pages/index.html',context)


def about(request):
    return render(request, 'pages/about.html')


def article(request):
    desc = request.GET.get('desc', '')
    if desc == '' :
        articles = Article.objects.all()
    else:
        articles = Article.objects.raw("select * from pages_article where description='" + desc + "'")
            
    context = {
        'articles': articles

    }
    return render(request, 'pages/article.html', context)





def details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article
    }

    return render(request, 'pages/details.html', context)


def contact(request):
    return render(request, 'pages/contact.html')
