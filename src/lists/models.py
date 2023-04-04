from django.db import models
from django.contrib.auth.models import User
from films.models import WatchedMovie
# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=500)
    movies = models.ManyToManyField(WatchedMovie)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    liked_by = models.ManyToManyField(User,related_name="liked_list_set")
    description = models.CharField(max_length=1000)