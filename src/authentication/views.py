from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from tmdbv3api import TMDb,Movie
import random
from itertools import chain
import os

tmdb = TMDb()
tmdb.api_key = os.environ.get("TMDB_API_KEY")
tmdb.language = 'en'
tmdb.debug = True


# Create your views here.
def home(request):
    movie = Movie()
    populer_movies = movie.popular()[0:6]

  
    if request.user.is_authenticated: #if user is already is_authenticated(looged in) then take user to home page
        context = {
            "upcoming": movie.upcoming(),
        }

        friends_movies = []
        followings = request.user.profile.following.all()
        for following in followings:
            if len(following.user.diary_log.order_by('-date','-created_at')[:3]) > 0:
                u = { 
                    "name":following.user.username,
                    "profile_picture":following.profile_picture.url, 
                    "movies":following.user.diary_log.order_by('-date','-created_at')[:3] 
                }
                friends_movies.append(u)
        recent = True
        if len(friends_movies) == 0:
            recent = False
        context["friends_movies"] = friends_movies
        context["recent_f"] = recent

        response = render(request,"main/home.html",context=context)
        response.set_cookie(key="username",value=request.user.username)
        return response



    populer_movies_mobile = movie.popular()[:4]
    
    context = {
        "movies": populer_movies,
        "movies_mobile": populer_movies_mobile,
        "list":[0,1,2,3],
        "for_cover": movie.popular()[random.randint(0,len(movie.popular())-1)]
    }
    
    return render(request,"authentication/index.html",context=context)
    
    
#------------------------------------------------------------------------

def signup(request):
    if request.method == "POST":
        
        user_details = {
            "username" : request.POST["username"],
            "first_name" : request.POST["first_name"],
            "last_name" : request.POST["last_name"],
            "email_address" : request.POST["email_address"],
            "password" : request.POST["password"],
            "confirm_password" : request.POST["confirm_password"],
        }
        
        if User.objects.filter(username=user_details["username"]):
            messages.error(request,f"Username:{user_details['username']} Already Exist! Try Different.")
            return redirect("authentication:home")
            
        if User.objects.filter(email=user_details["email_address"]):
            messages.error(request,f"{user_details['email_address']} This Email Already Registered!")
            return redirect("authentication:home")
        
        new_user = User.objects.create_user(user_details["username"],user_details["email_address"],user_details["password"])
        new_user.first_name = user_details["first_name"]
        new_user.last_name = user_details["last_name"]
        
        new_user.save()
        user = authenticate(username=user_details["username"], password=user_details["password"])
        login(request,user)
        messages.success(request,"Your Account is Created")
        
        
        
    return redirect("authentication:home")
        
    
    

#------------------------------------------------------------------------
def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username,password=password)
        
        
        if user is not None: #if user added right Credentials redirect user to root path again
            login(request,user)
            return redirect("authentication:home")
            
        else: #rediect him signin page with error messages
      
            messages.error(request,"invalid username or password")
            return redirect("authentication:home")
            
      
    return redirect("authentication:home")


#------------------------------------------------------------------------

def signout(request):
    logout(request)
    return redirect("authentication:home")
    