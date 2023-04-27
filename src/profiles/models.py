from django.db import models
from films.models import Film
from lists.models import List
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tmdbv3api import TMDb,Movie
from PIL import Image
import os
# Create your models here.



tmdb = TMDb()
tmdb.api_key = os.environ.get("TMDB_API_KEY")
tmdb.language = 'en'
tmdb.debug = True

def crop_image(image):
    width, height = image.size
    if width == height:
        return image
    offset  = int(abs(height-width)/2)
    if width>height:
        image = image.crop([offset,0,width-offset,height])
    else:
        image = image.crop([0,offset,width,height-offset])
    return image 
    
class Profile(models.Model):
    bio = models.CharField(max_length=1500,null=True,blank=True)
    country = models.CharField(max_length=50,blank=True)
    profile_picture = models.ImageField(upload_to="profile_picture/",default="default.png")
    cover_picture = models.ImageField(upload_to="cover_picture",default="default.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField("self", symmetrical=False,related_name="followers",blank=True)

    def save(self,*args,**kwargs):
        super().save()
        image = Image.open(self.profile_picture.path)
        image = crop_image(image)
        image.save(self.profile_picture.path)

    @staticmethod
    def filmExist(tmdb_id):
        film = Film.objects.filter(tmdb_id = tmdb_id)
        if film:
            return film[0]
        return False
    
    @classmethod
    def createFilm(cls,movie):
        film = cls.filmExist(movie["tmdb_id"]) 
        if film:
            return film

        m = Movie()
        mc = m.credits(movie["tmdb_id"])
        details = m.details(movie["tmdb_id"])
        directors = []
        for credit in mc.crew:
            if credit["job"] == "Director":
                directors.append(credit.original_name)
        director = ""
        release_year = details.release_date[:4]
        if len(directors) > 0:
            director = directors[0]
     
        film = Film.objects.create(tmdb_id=details.id,original_title=details.title,poster_path=details.poster_path,director=director,release_year=release_year)
        film.save()
        return film

     
    def add_watched_movie(self,movie):
        tmdb_id = movie["tmdb_id"]

        film = self.filmExist(tmdb_id)
        if film:
            film.watched_by.add(self.user)
            return film
        film = self.createFilm(movie)
        film.watched_by.add(self.user)
        return film

    def remove_watched_movie(self,tmdb_id):
        film = self.filmExist(tmdb_id) 
        if film and film.watched_by.filter(username=self.user.username):
            film.watched_by.remove(self.user)
            return True
        return False
        
    
    def add_to_watchlist(self,movie):
        tmdb_id = movie["tmdb_id"]

        film = self.filmExist(tmdb_id)
        if film and film.watchlisted_by.filter(username=self.user.username):
            film.watchlisted_by.add(self.user)
            return film
        film = self.createFilm(movie)
        film.watchlisted_by.add(self.user)

        
    def remove_from_watchlist(self,tmdb_id):
        film = self.filmExist(tmdb_id)
        print("heyy",film)
        if film and film.watchlisted_by.filter(username=self.user.username):
            film.watchlisted_by.remove(self.user)
            print("removed")
            return True
        return False
        
    
    def is_in_watchlist(self,tmdb_id):
        film = self.filmExist(tmdb_id)
        if film and film.watched_by.filter(username=self.user.username):
            return True
        return False
        
    def is_watched(self,tmdb_id):
        film = self.filmExist(tmdb_id)
        if film and film.watched_by.filter(username=self.username):
            return True
        return False
    
    def follow_user(self,username):
        user = User.objects.filter(username=username)[0]
        self.following.add(user.profile)
        return

    def unfollow_user(self,username):
        user = User.objects.filter(username=username)[0]
        self.following.remove(user.profile)
        
    

    def __str__(self):
        return f"Profile:{self.user.username}"



    def liked(self,movie):
        movie  = self.add_watched_movie(movie)
        movie.liked_by.add(self.user)
        return

        
    def unlike(self,movie_id):
        film = self.filmExist(movie_id)
        if film and film.liked_by.filter(username=self.user.username):
            film.liked_by.remove(self.user)
            return True
        return False

  
    def is_liked(self,tmdb_id):
        film = self.filmExist(tmdb_id)
        if film and film.liked_by.filter(username = self.user.username):
            return True
        return False

    def addList(self,list,movies):
        print("this is list info",list)  
        print("this is moves",movies)
        user_list = List.objects.create(name=list['list_name'],user=self.user,description=list['list_desc'])
        user_list.save()
        for movie in movies:
           list_movie = self.createFilm(movie)
           user_list.movies.add(list_movie)
        return user_list 

    def updateList(self,list,movies):
        user_list = List.objects.get(id=list["id"])
        user_list.name = list["list_name"]
        user_list.description = list["list_desc"]
        user_list.movies.clear()
        for movie in movies:
            list_movie = self.createFilm(movie)
            user_list.movies.add(list_movie)
        user_list.save()
        return

    def add_into_list(self,movie_id,list_id):
        movie = { 
            'tmdb_id': movie_id,
        }
        film = self.createFilm(movie)
        user_list = List.objects.get(id=list_id)
        user_list.movies.add(film)
        return user_list

class Top4Movies(models.Model):
    tmdb_id = models.IntegerField(unique=True) 
    poster_path = models.CharField(max_length=200)


class Top4(models.Model):
    one = models.ForeignKey(Top4Movies,on_delete=models.CASCADE,related_name="get_one",blank=True,null=True)
    two = models.ForeignKey(Top4Movies,on_delete=models.CASCADE,related_name="get_two",blank=True,null=True)
    three = models.ForeignKey(Top4Movies,on_delete=models.CASCADE,related_name="get_three",blank=True,null=True)
    four = models.ForeignKey(Top4Movies,on_delete=models.CASCADE,related_name="get_four",blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s top 4 movies"

