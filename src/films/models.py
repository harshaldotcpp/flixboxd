from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Film(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    original_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField() 
    watched_by = models.ManyToManyField(User,related_name="movies_set")
    liked_by = models.ManyToManyField(User,related_name="liked_movies_set",blank=True)
    watchlisted_by = models.ManyToManyField(User,related_name="watchlist")

    def post_review(self,review,user):
        return self.reviews_set.create(review=review,review_by=user)

    def __str__(self):
        return f"{self.original_title} by {self.director}"

    def getpercentage(sefl,got,total):
        if total == 0:
            return 0
        return (got/total) * 100
    
    def get_reviews(self):
        return self.reviews_set.all()
        
    def getAverageStars(self):
        all_rating = self.rating_set.all() 
        total = self.rating_set.count()
        ratings = [
            {
                "score": self.getpercentage(all_rating.filter(stars=0.5).count(), total), 
            },
            {
                "score": self.getpercentage(all_rating.filter(stars=1.0).count(), total) 
            },
            {
                "score": self.getpercentage(all_rating.filter(stars=1.5).count(), total)
            },
            {
                "score": self.getpercentage(all_rating.filter(stars=2.0).count(), total) 
            },
            {
                "score": self.getpercentage(all_rating.filter(stars=2.5).count(), total) 
            },
            {
                "score": self.getpercentage(all_rating.filter(stars=3.0).count(), total), 
            },
            {
                "score": self.getpercentage(all_rating.filter(stars=3.5).count(), total) 
            },
            {
                "score":self.getpercentage(all_rating.filter(stars=4.0).count() , total)
            },
            {
                "score": self.getpercentage(all_rating.filter(stars=4.5).count(),total)
            },
            {
                "score": self.getpercentage(all_rating.filter(stars=5).count(),total)
            },
        ]
        return ratings

    def averageRating(self):
        all_rating = self.rating_set.all()
        total = all_rating.count()
        sum = 0
        for rating in all_rating:
            sum = sum + rating.stars
        if total == 0:
            return 0
        return (sum/total)

 
 
 
class Rating(models.Model):
     stars = models.FloatField()
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     movie = models.ForeignKey(Film,on_delete=models.CASCADE)
     
     def __str__(self):
         return f"rating:{self.stars} movie: {self.movie} user:{self.user.username}"
 
 
        
        
class DiaryLog(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User,related_name='diary_log',on_delete=models.CASCADE)
    movie = models.ForeignKey(Film,related_name='diary_logs',on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.original_title} logged on {self.date} by {self.user.username}"
    
    
