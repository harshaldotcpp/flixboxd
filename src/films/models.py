from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class WatchedMovie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    original_title = models.CharField(max_length=100)
    overview = models.CharField(max_length=1000)
    tagline = models.CharField(max_length=50)
    rating = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)])
    poster_path = models.CharField(max_length=100)
    cover_path = models.CharField(max_length=100)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    watched_by = models.ManyToManyField(User,related_name="movies_set")
    liked_by = models.ManyToManyField(User,related_name="get_liked_movies",blank=True)
    
    def get_reviews(self):
        return self.reviews_set.all()
        
    def post_review():
        pass
        
    def __str__(self):
        return f"Movie:{self.original_title},Director:{self.director}"
 
 
 
class Watchlist(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    original_title = models.CharField(max_length=100,default="")
    poster_path = models.CharField(max_length=100)
    watch_listed = models.ManyToManyField(User,related_name="watchlist_set")
