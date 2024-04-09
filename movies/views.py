from django.shortcuts import render, redirect
from django.template import loader

from .models import Movie

def index(request):

    movies = Movie.objects.all()
    
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, pk):

    movie = Movie.objects.get(pk=pk)

    return render(request, 'movies/detail.html', {'movie': movie})

def create(request):

    if request.POST:
        print('save')
        # 

    return render('Hola pepito')

def update(request, pk):

    return render('Hola pepito')

def delete(request, pk):

    return redirect('movies/')