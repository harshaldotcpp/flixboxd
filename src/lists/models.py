from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ListMovie(models.Model):
    title = models.CharField(max_length=500)
    release_year = models.IntegerField()
    tmdb_id = models.IntegerField()
    poster_path = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Note(models.Model):
    note = models.CharField(max_length=1000)
    note_by = models.ForeignKey(User,on_delete=models.CASCADE)
    note_on = models.ForeignKey(ListMovie,on_delete=models.CASCADE)


class List(models.Model):
    name = models.CharField(max_length=500)
    movies = models.ManyToManyField(ListMovie)
    user = models.ForeignKey(User,related_name="lists",on_delete=models.CASCADE) 
    liked_by = models.ManyToManyField(User,related_name="liked_list_set")
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    update_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.user.username}"