from django.contrib import admin
from .models import Director, Genre, Movie

# Register your models here.


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country', 'birth_date')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'rating', 'genre', 'director')
    list_filter = ('genre', 'release_year')
    search_fields = ('title', 'description')