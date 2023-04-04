from django.db import models
from django.contrib.auth.models import User
from films.models import WatchedMovie
# Create your models here.

class ListMovie(models.Model):
    tmdb_id = models.IntegerField()
    note = models.IntegerField(max_length=500)
    poster_path = models.CharField(max_length=100)

class List(models.Model):
    name = models.CharField(max_length=500)
    movies = models.ManyToManyField(WatchedMovie)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    liked_by = models.ManyToManyField(User,related_name="liked_list_set")
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)