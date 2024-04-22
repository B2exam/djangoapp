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

def create(request):
    """
    Crea una película

    Variables:
        request (HttpRequest)
    """

    # Si recibimos datos por POST creamos la película 
    # con los datos proporcionados
    if request.POST:
        title = request.POST['title']
        actors = request.POST['actors']

        Movie.objects.create(title=title, actors=actors)
        return redirect('/')
    
    return render(request, 'movies/create.html')
