from django.shortcuts import render
from tmdbv3api import TMDb,Movie
import os

tmdb = TMDb()
tmdb.api_key = os.environ.get("TMDB_API_KEY")
tmdb.language = 'en'
tmdb.debug = True

# Create your views here.


def film(request,film_id):
    movie = Movie()
    m = movie.details(film_id)
   
    info = {
        "user_logged_in": request.user.is_authenticated,
        "film_name":film_id,
        "movie": m,
        "release_year": m.release_date[:4],
    }
    return render(request,"films/film.html",context=info)
    
    
    
def search_films(request,film_name):
    print(film_name)
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