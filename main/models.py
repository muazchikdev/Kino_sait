from django.db import models

# Create your models here.


class Director(models.Model):
    full_name = models.CharField('Полное имя', max_length=150)
    birth_date = models.DateField('Дата рождения')
    country = models.CharField('Страна', max_length=100)
    photo = models.ImageField('Фотография', upload_to='directors/', blank=True, null=True)

    class Meta:
        verbose_name = 'Режиссёр'
        verbose_name_plural = 'Режиссёры'

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='genres/', blank=True, null=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    duration = models.PositiveIntegerField('Длительность (мин)')
    release_year = models.PositiveIntegerField('Год выпуска')
    rating = models.PositiveSmallIntegerField('Рейтинг')
    poster = models.ImageField('Постер', upload_to='posters/', blank=True, null=True)

    vid_kino = models.FileField(
        'Фильм',
        upload_to='movies/',
        blank=True,
        null=True,
        help_text='Загрузите видеофайл (mp4, webm)'
    )

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies', verbose_name='Жанр')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', verbose_name='Режиссёр')

    added_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-added_at']

    def __str__(self):
        return self.title