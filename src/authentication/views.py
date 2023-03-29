from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from tmdbv3api import TMDb,Movie
import pprint
import random
import os

tmdb = TMDb()
tmdb.api_key = os.environ.get("TMDB_API_KEY")
tmdb.language = 'en'
tmdb.debug = True


# Create your views here.
def home(request):
    
  
    print(request.user.is_authenticated)
    if request.user.is_authenticated: #if user is already is_authenticated(looged in) then take user to home page
        return render(request,"main/home.html")
   
   #else user will to welcome page
    movie = Movie()
    populer_movies = movie.popular()[0:4]
    pprint.pprint(populer_movies)
    #print(populer_movies)
    context = {
        "movies": populer_movies,
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
            return redirect ("authentication:signup")
            
        if User.objects.filter(email=user_details["email_address"]):
            messages.error(request,f"{user_details['email_address']} This Email Already Registered!")
            return redirect("authentication:signup")
        
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
    print("signin")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username,password=password)
        print(user)
        
        if user is not None: #if user added right Credentials redirect user to root path again
            login(request,user)
            print("ok")
            return redirect("authentication:home")
            
        else: #rediect him signin page with error messages
      
            messages.error(request,"invalid username or password")
            return redirect("authentication:home")
            
        
    return render(request,"authentication/index.html")


#------------------------------------------------------------------------

def signout(request):
    logout(request)
    return redirect("authentication:home")
    