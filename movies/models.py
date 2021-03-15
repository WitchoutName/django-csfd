from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


def poster_path(a, b):
    return f"film/{a.film.id}/poster/{b}"


def file_path(a, b):
    return f"film/{a.film.id}/attach/{b}"


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Genre ame", help_text="Genre of a film.")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titl")
    plot = models.TextField(blank=True, null=True, help_text="title")
    release_date = models.DateField(blank=True, null=True, help_text="YYYY-MM-DD", verbose_name="Date")
    length = models.IntegerField(blank=True, null=True, help_text="full minutes", verbose_name="length")
    rating = models.FloatField(default=2.5, validators=[MinValueValidator(1.), MaxValueValidator(5.)], null=True, help_text="1-5", verbose_name="rating")
    poster = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Poster")
    genres = models.ManyToManyField(Genre, help_text="genres", verbose_name="genres")

    class Meta:
        ordering = ["title", "-release_date"]

    def __str__(self):
        return f"{self.title}, year: {self.release_date.year}, rate: {self.rating}"

    def get_absolute_url(self):
        return reverse("film-detail", args=[str(self.id)])


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titl")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=file_path)
    TYPES = [["audio","Audio"], ["image","Image"], ["text","Text"], ["video","Video"], ["other","Other"]]
    type = models.CharField(max_length=5, choices=TYPES, blank=True, default="Image", help_text="file type", verbose_name="file type")
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    class Meta:
        ordering = ["last_update"]

    def __str__(self):
        return f"{self.title}, ({self.type})"