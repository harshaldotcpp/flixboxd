from films.models import WatchedMovie
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    review = models.CharField(max_length=1000)
    movie = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_reviews")
    date = models.DateTimeField(auto_now_add=True)
    review_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews_set")
    
   
    
    def __str__(self):
        return f"review:{ self.review},movie:{self.movie.original_title}"