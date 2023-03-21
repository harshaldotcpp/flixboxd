from films.models import WatchedMovie
from django.db import models

# Create your models here.

class Review(models.Model):
    review = models.CharField(max_length=1000)
    movie = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE)
    
   
    
    def __str__(self):
        return f"review:{ self.review},movie:{self.movie.original_title}"