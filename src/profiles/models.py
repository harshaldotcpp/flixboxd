from django.db import models
from films.models import WatchedMovie
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


    
    
    
class Profile(models.Model):
    bio = models.CharField(max_length=1500,null=True,blank=True)
    country = models.CharField(max_length=50,blank=True)
    profile_picture = models.ImageField(upload_to="profile_picture/",default="default.png")
    cover_picture = models.ImageField(upload_to="cover_picture",default="default.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    
    def add_movie(self,tmdb_id,title, overview,tagline,rating,poster,cover,date,director,liked=False):
        self.user.movies_set.create(tmdb_id=tmdb_id,original_title=title, overview=overview, tagline=tagline,rating=rating,poster_path=poster,cover_path=cover,release_date=date, director=director)
    
    
    def is_watched(self,tmdb_id):
        if self.user.movies_set.filter(tmdb_id=tmdb_id).count() == 0:
            return False
        return True
    
    def follow_user(self,user):
        self.user.following_set.create(following_id=user)
        
    
    def unfollow_user(self,username):
        followings = self.user.following_set.all()
        for follower in followings:
            if(follower.following_id.username == username):
                return follower.delete()
        return None


    def get_followers(self):
        followers = []
       
        for f in self.user.follower_set.all():
            followers.append(f.user_id)
        return followers

    def get_following(self):
        following = []
        for f in self.user.following_set.all():
            following.append(f.following_id)
        return following

    def __str__(self):
        return f"Profile:{self.user.username}"

    def liked_movie(self):
        pass

    def get_user_movies(self):
        pass
  
  
    
class Top4(models.Model):
    one = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_one",blank=True,null=True)
    two = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_two",blank=True,null=True)
    three = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_three",blank=True,null=True)
    four = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_four",blank=True,null=True)
    user = models.OneToOneField(Profile,on_delete=models.CASCADE)


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User,related_name="following_set",on_delete=models.CASCADE)
    following_id = models.ForeignKey(User,related_name="follower_set",on_delete=models.CASCADE)
 
    class Meta:
        unique_together = ("user_id", "following_id")
