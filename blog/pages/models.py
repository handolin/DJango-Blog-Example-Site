from django.db import models
from random import choices

# Create your models here.

KATEGORILER = (
    ('Gezi', 'Gezi'),
    ('Yemek', 'Yemek'),
    ('Film', 'Film'),
    ('Tiyatro','Tiyatro'),
    ('Müzik', 'Müzik'),
    ('Kitap', 'Kitap')
)

class Article(models.Model):
    name = models.CharField(max_length=100, verbose_name='Makale Adı')
    description = models.CharField(max_length=100, choices=KATEGORILER,  verbose_name='Kategori')
    image = models.ImageField(
        verbose_name="Makale Fotoğrafı", upload_to="static/uploads", null=False)
    # image = models.CharField(max_length=50, verbose_name='Makale Fotoğrafı')
    article_details = models.TextField(verbose_name='Makale')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Eklenme Tarihi')
    isPublished = models.BooleanField(
        default=True, verbose_name='Yayında')


def __str__(self):
    return self.name


def get_image_path(self):
    return '/img/' + self.image
