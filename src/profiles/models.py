from django.db import models
from films.models import WatchedMovie,Watchlist
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
# Create your models here.



    
class Profile(models.Model):
    bio = models.CharField(max_length=1500,null=True,blank=True)
    country = models.CharField(max_length=50,blank=True)
    profile_picture = models.ImageField(upload_to="profile_picture/",default="default.png")
    cover_picture = models.ImageField(upload_to="cover_picture",default="default.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField("self", symmetrical=False,related_name="followers",blank=True,null=True)
 
    
  
    
      
    def add_watched_movie(self,movie):
        db_movie = WatchedMovie.objects.filter(tmdb_id=movie["tmdb_id"])
        if db_movie:
            self.user.movies_set.add(db_movie[0])
            return
        
        tmdb_id = movie["tmdb_id"]
        title = movie["original_title"]
        poster_path = movie['poster_path']
        director = movie['director']
        
        return self.user.movies_set.create(tmdb_id=tmdb_id,original_title=title,poster_path=poster_path, director=director)
        
    
    def remove_watched_movie(self,tmdb_id):
        db_movie = self.user.movies_set.filter(tmdb_id=tmdb_id)
        if db_movie: #safety check
            self.user.movies_set.remove(db_movie[0])
            return True
     
        return False
        
    
    def add_to_watchlist(self,movie):
        tmdb_id = movie["tmdb_id"]
        title = movie["original_title"]
        poster_path = movie['poster_path']
    
        db_movie = Watchlist.objects.filter(tmdb_id=movie["tmdb_id"])
        
        if db_movie:
            self.user.watchlist_set.add(db_movie[0])
            return

        #self.user.watchlist_set.create(tmdb_id=tmdb_id,original_title=title,poster_path=poster_path)
        #return
        
        
    def remove_from_watchlist(self,tmdb_id):
        db_movie = self.user.watchlist_set.filter(tmdb_id=tmdb_id)
        if db_movie:
            self.user.watchlist_set.remove(db_movie[0])
            return True
        return False
    
    def is_in_watchlist(self,tmdb_id):
        if self.user.watchlist_set.filter(tmdb_id=tmdb_id).count() == 0:
            return False
        return True

        
    def is_watched(self,tmdb_id):
        if self.user.movies_set.filter(tmdb_id=tmdb_id).count() == 0:
            return False
        return True
    
    def follow_user(self,username):
        user = User.objects.filter(username=username)[0]
        self.following.add(user.profile)
        return

    def unfollow_user(self,username):
        user = User.objects.filter(username=username)[0]
        self.following.remove(user.profile)
        
    

    def __str__(self):
        return f"Profile:{self.user.username}"

    def liked_movie(self):
        pass

    def get_user_movies(self):
        pass

    def liked(self,movie):
        db_movie = WatchedMovie.objects.filter(tmdb_id=movie["tmdb_id"])
        
        if db_movie:
            self.user.liked_movies_set.add(db_movie[0])
            return
        
        tmdb_id = movie["tmdb_id"]
        title = movie["original_title"]
        poster_path = movie['poster_path']
        director = movie['director']
        
        return self.user.liked_movie_set.create(tmdb_id=tmdb_id,original_title=title,poster_path=poster_path, director=director)
        
    def unlike(self,movie_id):
        db_movie = self.user.liked_movies_set.filter(tmdb_id = movie_id)
       
        if db_movie:
            self.user.liked_movies_set.remove(db_movie)
            return True
        return False
  
    def is_liked(self,movie_id):
        if self.user.liked_movies_set.filter(tmdb_id = movie_id):
            return True
        return False
  
    
class Top4(models.Model):
    one = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_one",blank=True,null=True)
    two = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_two",blank=True,null=True)
    three = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_three",blank=True,null=True)
    four = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_four",blank=True,null=True)
    user = models.OneToOneField(Profile,on_delete=models.CASCADE)

