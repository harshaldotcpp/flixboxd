from django.db import models
from films.models import WatchedMovie,Film
from lists.models import List,ListMovie
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tmdbv3api import TMDb,Movie
import os
# Create your models here.



tmdb = TMDb()
tmdb.api_key = os.environ.get("TMDB_API_KEY")
tmdb.language = 'en'
tmdb.debug = True


    
class Profile(models.Model):
    bio = models.CharField(max_length=1500,null=True,blank=True)
    country = models.CharField(max_length=50,blank=True)
    profile_picture = models.ImageField(upload_to="profile_picture/",default="default.png")
    cover_picture = models.ImageField(upload_to="cover_picture",default="default.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField("self", symmetrical=False,related_name="followers",blank=True)
 
    
  
    def createFilm(self,movie):
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

    def filmExist(self,tmdb_id):
        film = Film.objects.filter(tmdb_id = tmdb_id)
        if film:
            return film[0]
        return False
      
    def add_watched_movie(self,movie):
        tmdb_id = movie["tmdb_id"]
        title = movie["original_title"]
        poster_path = movie['poster_path']
        director = movie['director']
        release_year = movie['release_year']

        film = Film.objects.filter(tmdb_id= tmdb_id)

        if film:
            watched_film = WatchedMovie.objects.filter(film = film[0])
            if watched_film:
                watched_film[0].watched_by.add(self.user)
                return watched_film[0]
            watched_film = WatchedMovie.objects.create(film=film[0])
            watched_film.save()
            watched_film.watched_by.add(self.user)
            return watched_film

        
        film = self.createFilm(movie) 
        watched_film = WatchedMovie.objects.create(film=film)
        watched_film.save()
        watched_film.watched_by.add(self.user)
        return watched_film
         
         
    
    def remove_watched_movie(self,tmdb_id):

        film = Film.objects.filter(tmdb_id= tmdb_id)
        if film:
            db_movie = self.user.movies_set.filter(film=film[0])
            if db_movie: #safety check
                self.user.movies_set.remove(db_movie[0])
                return True
     
        return False
        
    
    def add_to_watchlist(self,movie):
        film = self.filmExist(movie["tmdb_id"])
        if film:
            watched_film = WatchedMovie.objects.filter(film=film)
            if watched_film:
                self.user.watchlist.add(watched_film[0])
                return watched_film[0]
            watched_film = WatchedMovie.objects.create(film=film)
            watched_film.save()
            self.user.watchlist.add(watched_film)
            return watched_film
        film = self.createFilm(movie)
        watched_film = WatchedMovie.objects.create(film=film)
        watched_film.save()
        self.user.watchlist.add(watched_film)
        return watched_film
            

    

        
        
    def remove_from_watchlist(self,tmdb_id):
        pass 
    
    def is_in_watchlist(self,tmdb_id):
        pass

        
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



    def liked(self,movie):
        movie  = self.add_watched_movie(movie)
        self.user.liked_movies_set.add(movie)
        return

        
    def unlike(self,movie_id):
        film = Film.objects.filter(tmdb_id=movie_id)
        if film:
            db_movie = self.user.liked_movies_set.filter(film = film[0])
            if db_movie:
                self.user.liked_movies_set.remove(db_movie[0])
                return True
        return False
  
    def is_liked(self,movie_id):
        if self.user.liked_movies_set.filter(tmdb_id = movie_id):
            return True
        return False

    def addList(self,list,movies):
        print("this is list info",list)  
        print("this is moves",movies)
        user_list = List.objects.create(name=list['list_name'],user=self.user,description=list['list_desc'])
        user_list.save()
        for movie in movies:
           list_movie = ListMovie.objects.filter(tmdb_id = movie["tmdb_id"])
           if list_movie:
               user_list.movies.add(list_movie[0]) 
           else:
               new_list_movie = ListMovie.objects.create(title=movie["title"],release_year=movie['release_year'],tmdb_id=movie["tmdb_id"],poster_path=movie["poster_path"])
               new_list_movie.save()
               user_list.movies.add(new_list_movie)
        return 

    def updateList(self,list,movies):
        user_list = List.objects.get(id=list["id"])
        user_list.name = list["list_name"]
        user_list.description = list["list_desc"]
        user_list.movies.clear()
        for movie in movies:
            list_movie = ListMovie.objects.filter(tmdb_id = movie["tmdb_id"])
            if list_movie:
                user_list.movies.add(list_movie[0]) 
            else:
                new_list_movie = ListMovie.objects.create(title=movie["title"],release_year=movie['release_year'],tmdb_id=movie["tmdb_id"],poster_path=movie["poster_path"])
                new_list_movie.save()
                user_list.movies.add(new_list_movie)
        user_list.save()
        return

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

