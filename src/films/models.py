from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class WatchedMovie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    original_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    watched_by = models.ManyToManyField(User,related_name="movies_set")
    liked_by = models.ManyToManyField(User,related_name="liked_movies_set",blank=True)
   
    
    def get_reviews(self):
        return self.reviews_set.all()
        
    def post_review(self,review,user):
        return self.reviews_set.create(review=review,review_by=user)

        
    def __str__(self):
        return f"Movie:{self.original_title},Director:{self.director}"
 
 
 
class Rating(models.Model):
     stars = models.FloatField()
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     movie = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE)
     
     def __str__(self):
         return f"rating:{self.stars} user:{self.user.username}"
 
 
class Watchlist(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    original_title = models.CharField(max_length=100,default="")
    poster_path = models.CharField(max_length=100)
    watch_listed = models.ManyToManyField(User,related_name="watchlist_set")
    
    def __str__(self):
        return f"movie:{self.original_title}"
        
        
class DiaryLog(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User,related_name='diary_log',on_delete=models.CASCADE)
    movies = models.ManyToManyField(WatchedMovie)
    
    
