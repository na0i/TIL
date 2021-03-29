from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

#
@login_required
#
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        #
        if form.is_valid():
        #
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

#
@login_required
#
@require_http_methods(['GET', 'POST'])
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance = movie)
        # form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance = movie)
        # movies = Movie.objects.all()
        # form = MovieForm()
    context = {
        # 'movies' : movies,
        'form' : form,
        'movie' : movie,
    }
    return render(request, 'movies/update.html' context)


@require_POST
def delete(request, movie_pk):
    #
    if request.user.is_authenticated:
    #
        movie = get_object_or_404(Movie, pk = movie_pk)
        movie.delete()
    return redirect('movies:index')