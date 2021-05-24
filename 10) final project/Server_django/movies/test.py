from .models import Movie

movies = Movie.objects.all()

print(movies)