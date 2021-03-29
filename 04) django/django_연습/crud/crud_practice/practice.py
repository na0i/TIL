@require_safe
def index(request):
    movies = Moive.object.all()
    context = {
        'movies' : movies
    }
    return render(request, 'index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie:detail', movie.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context ={
        'movie' : movie
    }
    return render(request, 'detail.html', context)

@login_required
@require_http_methos(['GET', 'POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=movie.pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('detail', movie.pk)
    else:
        form = ArticeForm(instance=movie)
    context = {
        'movie' : movie,
        'form' : form,
    }
    return render(request, 'update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated():
        movie = get_object_or_404(Movie, pk=movie.pk)
        movie.delete()
    return redirect('movie:index')