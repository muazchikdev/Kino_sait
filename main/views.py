from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from .models import Movie, Genre
from django.db.models import Q
from .models import Movie

# Create your views here.


def movie_list(request):
    """Главная: список фильмов + поиск + фильтр по жанру"""
    query = request.GET.get('q', '').strip()
    genre_id = request.GET.get('genre')

    movies = Movie.objects.all()

    if genre_id:
        movies = movies.filter(genre_id=genre_id)

    if query:
        q = query.lower()
        movies = movies.annotate(
            t=Lower('title'),
            d=Lower('description'),
            dir=Lower('director__full_name'),
            g=Lower('genre__name'),
        ).filter(
            Q(t__contains=q) |
            Q(d__contains=q) |
            Q(dir__contains=q) |
            Q(g__contains=q)
        ).distinct()

    genres = Genre.objects.all()
    current_genre = None
    if genre_id:
        current_genre = Genre.objects.filter(id=genre_id).first()

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'query': query,
        'genres': genres,
        'current_genre': current_genre,
    })


def movie_detail(request, pk):
    """Страница фильма с плеером"""
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})