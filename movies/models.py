from django.db import models

class Movie (models.Model):



    title = models.CharField('Título', max_length=500)
    actors = models.CharField('Actores', max_length=2000)