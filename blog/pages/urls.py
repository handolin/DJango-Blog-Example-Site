from django.urls import path
from . import views


# http: // 127.0.0.1: 8000/

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('article', views.article, name='article'),
    path('<int:article_id>', views.details, name='details'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

]
