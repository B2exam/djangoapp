from django.shortcuts import render, redirect
from django.template import loader

from .models import Movie

def index(request):
    """
    Vista en modo listado de todas las películas registradas

    Variables:
        request (HttpRequest)
    """

    # Consulta para recoger el total de películas
    movies = Movie.objects.all()
    
    return render(request, 'movies/index.html', {'movies': movies})
