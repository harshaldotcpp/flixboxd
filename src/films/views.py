from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect  
from .models import WatchedMovie
from django.shortcuts import render
from tmdbv3api import TMDb,Movie
from django.contrib import messages
import random
import json
import os

tmdb = TMDb()
tmdb.api_key = os.environ.get("TMDB_API_KEY")
tmdb.language = 'en'
tmdb.debug = True

# Create your views here.

def watched(request):
    if request.method == "POST":
       
        obj = json.load(request)
        movie_add = obj["add"]
        
        if movie_add:
            movieInfo = {
                "tmdb_id": obj["tmdb_id"],
                "original_title": obj["title"].strip("\""),
                "poster_path" : obj["poster_path"].strip("\""),
                "director": obj["director"].strip("\"")
            
            }
            request.user.profile.add_watched_movie(movieInfo)
            request.user.profile.remove_from_watchlist(obj["tmdb_id"])
            
            response_data = {
                "status": "succesfull",
                "message": "added_to_watched"
            }
            return HttpResponse(json.dumps(response_data),content_type='application/json')
        
        request.user.profile.unlike(obj["tmdb_id"])   
        request.user.profile.remove_watched_movie(obj["tmdb_id"])
        
       
    return HttpResponse("error")



def liked(request):

    if request.method == "POST":
       
        obj = json.load(request)
        movie_add = obj["add"]
        
        if movie_add:
            movieInfo = {
                "tmdb_id": obj["tmdb_id"],
                "original_title": obj["title"].strip("\""),
                "poster_path" : obj["poster_path"].strip("\""),
                "director": obj["director"].strip("\"")
            
            }
            request.user.profile.liked(movieInfo)
            request.user.profile.add_watched_movie(movieInfo)
            
            response_data = {
                "status": "succesfull",
                "message": "added_to_watched"
            }
            return HttpResponse(json.dumps(response_data),content_type='application/json')
        
        request.user.profile.unlike(obj["tmdb_id"])
        
    return HttpResponse("error")   
        


def watchlist(request):
    if request.method == "POST":
        print("hello world")
        obj = json.load(request)
        movie_add = obj["add"]

        if movie_add:
            movie_info = {
                "tmdb_id": obj["tmdb_id"],
                "original_title": obj["title"].strip("\""),
                "poster_path": obj["poster_path"].strip("\"")
            }
            request.user.profile.add_to_watchlist(movie_info)
            response_data = {
                "status": "succesfull",
                "message": "added_to_watched"
            }

            return HttpResponse(json.dumps(response_data),content_type='application/json')

        request.user.profile.remove_from_watchlist(obj["tmdb_id"])

    return HttpResponse("watchlist error")


def addReview(request):
    if(request.method == "POST"):
        movie_info = {
            "tmdb_id": request.POST["tmdb_id"],
            "original_title": request.POST["title"],
            "poster_path": request.POST["poster_path"],
            "director": request.POST["director"],
            "review": request.POST['review'],
        }
        
        print(movie_info) 
        movie = request.user.profile.add_watched_movie(movie_info)
        movie.post_review(movie_info["review"],request.user)
    
    url = f"/film/{request.POST['tmdb_id']}"
    return redirect(url)

    
     


def film(request,film_id):

    movie = Movie()
    m = movie.details(film_id)
    mc = movie.credits(film_id)
    similar_movies = movie.similar(film_id)
   
    directors = []
    for credit in mc.crew:
        if credit["job"] == "Director":
            directors.append(credit.original_name)
        
    if len(directors) == 0:
        directors = [""]
    
    
    info = {
        "movie": m,
        "release_year": m.release_date[:4],
        "director": directors[0],
        "similar_movies": similar_movies,

        
    }

    reviews = []
    requested_movie = WatchedMovie.objects.filter(tmdb_id=m.id)
    if requested_movie:
        reviews = requested_movie[0].reviews_set.all()

    review_len = len(reviews)
    info["reviews"] = reviews
    info["reviews_len"] = len(reviews)

    response = render(request,"films/film.html",context=info)
    response.set_cookie(key="movie_name",value=m.title)
    response.set_cookie(key="id",value=m.id)
    response.set_cookie(key="poster_path",value = m.poster_path)
    response.set_cookie(key="director",value= directors[0])
   
    return response
    





def search_films(request,film_name):
  
    movie = Movie()
    movies = movie.search(film_name)
   
    
    for m in movies:
        credits = movie.credits(m.id)
        directors  = []
        a_titles = ""
        for credit in credits.crew:
            if credit["job"] == "Director":
                directors.append(credit.original_name)
        for title in movie.alternative_titles(m.id)["titles"]:
            a_titles += title["title"] +", "
        
        if len(directors) > 0:    
            m["director"] = directors[0]
        m["release_year"] = m.release_date[:4]
        m["a_titles"] = a_titles
        
    
   
    
    context = {
        "search_value":film_name,
        "movies": movies,
        "user_logged_in": request.user.is_authenticated,
        "len": len(movies),
    }
    return render(request,"films/search_page.html",context=context)



def  showWatchlist(request,username):
    user = User.objects.get(username=username)
    movies = user.watchlist_set.all()


    context = {
        "movies": movies,
        "len": len(movies),
        "user": user,
        
    }
    return render(request,"films/watchlist.html",context=context)


def showWatched(request,username):
    user = User.objects.get(username=username)
    movies = user.movies_set.all()

    context={
        "movies": movies,
        "len" : len(movies),
        "user": user
    }

    return render(request,"films/watched_films.html",context=context);



def showLiked(request,username):
   pass