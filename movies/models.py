from django.db import models

class Movie (models.Model):
    """
    Movie es el modelo que define una película. 
    Se define a través de las siguientes variables

    Variables:
        title (CharField): Título de la película
        actors (CharField): Lista de actores, en texto plano
    """

    title = models.CharField('Título', max_length=500)
    actors = models.CharField('Actores', max_length=2000)