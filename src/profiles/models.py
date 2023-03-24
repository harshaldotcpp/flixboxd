from django.db import models
from films.models import WatchedMovie
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    bio = models.CharField(max_length=1500,null=True)
    country = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="profile_picture/",default="default.png")
    cover_picture = models.ImageField(upload_to="cover_picture",default="default.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def add_movie(self,tmdb_id,title, overview,tagline,rating,poster,cover,date,director,liked=False):
        self.user.movies_set.create(tmdb_id=tmdb_id,original_title=title, overview=overview, tagline=tagline,rating=rating,poster_path=poster,cover_path=cover,release_date=date, director=director)
    
    def is_watched(tmdb_id):
        if self.user.movies_set.filter(tmdb_id).count() == 0:
            return False
        return True


    def liked_movie(self):
        pass

    def get_user_movies():
        pass
    
class Top4(models.Model):
    one = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_one",blank=True,null=True)
    two = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_two",blank=True,null=True)
    three = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_three",blank=True,null=True)
    four = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_four",blank=True,null=True)
    user = models.OneToOneField(Profile,on_delete=models.CASCADE)