from django.http import  HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect  
from django.shortcuts import render
from django.contrib import messages
from .models import Rating,DiaryLog,Film
from tmdbv3api import TMDb,Movie
import datetime
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
            }

            request.user.profile.add_watched_movie(movieInfo)
            request.user.profile.remove_from_watchlist(obj["tmdb_id"])
            response_data = {
                "status": "succesfull",
                "message": "Added to watched"
            }
            return HttpResponse(json.dumps(response_data),content_type='application/json')


        movie = Film.objects.filter(tmdb_id=obj["tmdb_id"])

        if movie and Rating.objects.filter(movie=movie[0],user=request.user):
            return HttpResponse(json.dumps({"status":"failed","message":"theres activity on this movie"}),content_type="application/json")

        request.user.profile.unlike(obj["tmdb_id"])   
        request.user.profile.remove_watched_movie(obj["tmdb_id"])
        return HttpResponse(json.dumps({"status":"succesfull","message":"removed from watched"}),content_type="application/json")
        
       
    return HttpResponse("error")



def liked(request):

    if request.method == "POST":
       
        obj = json.load(request)
        movie_add = obj["add"]
        
        if movie_add:
            movieInfo = {
                "tmdb_id": obj["tmdb_id"],
            }
            request.user.profile.liked(movieInfo)
            request.user.profile.add_watched_movie(movieInfo)
            
            response_data = {
                "status": "succesfull",
                "message": "liked the movie"
            }
            return HttpResponse(json.dumps(response_data),content_type='application/json')
        
        request.user.profile.unlike(obj["tmdb_id"])
        return HttpResponse(json.dumps({"status":"succesfull","message":"unlike the movie"}),content_type='application/json')
        
    return HttpResponse("error")   
        


def watchlist(request):
    if request.method == "POST":
        obj = json.load(request)
        movie_add = obj["add"]
        if movie_add:
            movie_info = {
                "tmdb_id": obj["tmdb_id"],
            }

            request.user.profile.add_to_watchlist(movie_info)
            response_data = {
                "status": "succesfull",
                "message": "Added to watched"
            }

            return HttpResponse(json.dumps(response_data),content_type='application/json')

        request.user.profile.remove_from_watchlist(obj["tmdb_id"])
        return HttpResponse(json.dumps({"status":"succusfull","message":"Removed from watchlist"}),content_type='application/json')
        

    return HttpResponse("watchlist error")


def addReview(request):

    if(request.method == "POST"):
        url = f"/film/{request.POST['tmdb_id']}"
        movie_info = {
            "review": request.POST["review"],
            "tmdb_id": request.POST["tmdb_id"],
             "date": request.POST["date"]
        }
       

        if len(movie_info["review"]) != 0:
            movie = request.user.profile.add_watched_movie(movie_info)
            movie.post_review(movie_info["review"],request.user)
            messages.success(request,"Review Added")

        if request.POST.get("shouldlog") is not None:
            movie = request.user.profile.add_watched_movie(movie_info)
            log_date = datetime.datetime.strptime(movie_info["date"],'%Y-%m-%d').date()
            user_diary = request.user.diary_log.filter(date=log_date)
            if user_diary:
                if user_diary.filter(movie = movie):
                    messages.error(request,"This Movie Already Logged on This Day")
                    return redirect(url)

            diaryLog = DiaryLog.objects.create(date=log_date,user=request.user,movie=movie)
            diaryLog.save()
            messages.success(request,"Added in logs")
            
        return redirect(url)

    return redirect("/")

    
     


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
        "user_lists": request.user.lists.all(),
    }

    print(info["user_lists"])

    reviews = []
    myReviews = []
    requested_movie = Film.objects.filter(tmdb_id=m.id)
    if requested_movie:
        reviews = requested_movie[0].reviews_set.all()
        if request.user.is_authenticated:
            myReviews = request.user.reviews_set.filter(movie=requested_movie[0])

    review_len = len(reviews)
    info["reviews"] = reviews
    info["reviews_len"] = len(reviews)
    info['my_reviews'] = myReviews


    response = render(request,"films/film.html",context=info)
    response.set_cookie(key="id",value=m.id)
   
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
    user = User.objects.filter(username=username)

    if user:

        movies = user[0].watchlist.all()
        context = {
            "movies": movies,
            "len": len(movies),
            "search_user": user[0],
            "page": "watchlist"
            
        }
        return render(request,"films/watchlist.html",context=context)

    return render(request,"profile_page/error.html") 


def showWatched(request,username):
    user = User.objects.filter(username=username)

    if user:
        movies = user[0].movies_set.all()

        context={
            "movies": movies,
            "len" : len(movies),
            "search_user": user[0],
            "page": "watched"
        }
    
        return render(request,"films/watched_films.html",context=context);

    return render(request,"profile_page/error.html") 

def diary(request,username):
    user = User.objects.filter(username=username)
    diary_len = 0

    if user:
        diary_logs = user[0].diary_log.order_by('-date','-created_at')
        if diary_logs:
            diary_len = len(diary_logs)
        
        for logs in diary_logs:
            print(logs.movie.poster_path)
        context = {
            "page" : "diary",
            "diary_log": diary_logs,
            "search_user":user[0],
            "new_month":0
        }
        return render(request,"films/diary.html",context=context)
    return render(request,"profile_page/error.html")

def showLiked(request,username):
   pass



def rating(request):
    if request.method == "POST":
        obj = json.load(request)

        movieInfo = {
            "rating":obj["rating"],
            "tmdb_id": obj["tmdb_id"],
        }
    
        movie = request.user.profile.add_watched_movie(movieInfo)
        user_rating = Rating.objects.filter(movie=movie,user=request.user)

        if user_rating:
            user_rating[0].stars = movieInfo["rating"]
            user_rating[0].save()
            return HttpResponse(json.dumps({"status":"succesfull","message":"rating updated"}),content_type="application/json")

        rating = Rating.objects.create(stars=movieInfo["rating"],movie=movie,user=request.user)
        rating.save()
        return HttpResponse(json.dumps({"status":"succusfull","message":"rating added"}),content_type="application/json")


    return HttpResponse(json.dumps({"status":"failed","message":"get request not allowed"}),content_type='application/json')


def removeRating(request):
    if request.method == "POST":
        obj = json.load(request)
        film = request.user.profile.filmExist(obj["tmdb_id"])
        if film:
            rating = Rating.objects.filter(movie=film,user=request.user)
            if rating:
                rating[0].delete()
        return HttpResponse(json.dumps({"status":"succesfull","message":"rating removed"}),content_type="application/json")


        return HttpResponse(json.dumps({"status":"failed","message":"there is no rating for this movie"}),content_type='application/json')








