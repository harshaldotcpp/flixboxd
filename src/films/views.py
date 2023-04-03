from django.shortcuts import render
from tmdbv3api import TMDb,Movie
import os
from django.http import JsonResponse
import json
from django.http import HttpResponse

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
                "original_title": obj["title"],
                "poster_path" : obj["poster_path"],
                "director": obj["director"]
            
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
    print("hello")
    if request.method == "POST":
       
        obj = json.load(request)
        movie_add = obj["add"]
        
        if movie_add:
            movieInfo = {
                "tmdb_id": obj["tmdb_id"],
                "original_title": obj["title"],
                "poster_path" : obj["poster_path"],
                "director": obj["director"]
            
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
        


def film(request,film_id):
    
    movie = Movie()
    m = movie.details(film_id)
    mc = movie.credits(film_id)
   
    directors = []
    for credit in mc.crew:
        if credit["job"] == "Director":
            directors.append(credit.original_name)
        
    if len(directors) == 0:
        directors = [""]
    
    watch_btn = ""
    watch_checked = ""
    liked_checked = "none"
    liked_btn = ""
    if request.user.is_authenticated:
        if(request.user.profile.is_watched(film_id)):
            watch_btn = "fill-letterboxd-4"
            watch_checked = "checked"
        if(request.user.profile.is_liked(film_id)):
            liked_btn = "fill-letterboxd-5"
            liked_checked = "checked"
            
       
        
   
    info = {
        "user_logged_in": request.user.is_authenticated, 
        "movie": m,
        "release_year": m.release_date[:4],
        "director": directors[0],
        "watch_btn": watch_btn,
        "watched_checked" : watch_checked,
        "liked_check": liked_checked,
        "liked_btn": liked_btn,
    }
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
        "user_logged_in": request.user.is_authenticated,
        "search_value":film_name,
        "movies": movies,
        "user_logged_in": request.user.is_authenticated,
        "len": len(movies),
    }
    return render(request,"films/search_page.html",context=context)