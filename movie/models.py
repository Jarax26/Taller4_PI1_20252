from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.CharField(max_length=250)
    poster_image = models.ImageField(upload_to='movie/posters/', blank=True, null=True)
    url = models.URLField(blank=True)