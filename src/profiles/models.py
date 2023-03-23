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
    
    
    
class Top4(models.Model):
    one = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_one",blank=True,null=True)
    two = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_two",blank=True,null=True)
    three = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_three",blank=True,null=True)
    four = models.ForeignKey(WatchedMovie,on_delete=models.CASCADE,related_name="get_four",blank=True,null=True)
    user = models.OneToOneField(Profile,on_delete=models.CASCADE)
