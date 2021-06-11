from django.db import models

class Article(models.Model):
    nomi = models.CharField('Nomi', max_length=80)
    muallif = models.CharField('Muallif:', max_length=50)
    tarif = models.TextField(null=True)
    rasm = models.ImageField(null=True)
    vaqt = models.DateTimeField(null=True)
