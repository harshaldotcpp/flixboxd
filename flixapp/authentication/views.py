from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    if request.user.is_authenticated: #if user is already is_authenticated(looged in) then take user to home page
        return render(request,"home_page/home.html")
   
   #else user will to welcome page
    return render(request,"authentication/index.html")
    
    
#------------------------------------------------------------------------

def signup(request):
    
    if request.method == "POST":
        print("hello")
        user_details = {
            "username" : request.POST["username"],
            "first_name" : request.POST["first_name"],
            "last_name" : request.POST["last_name"],
            "email_address" : request.POST["email_address"],
            "password" : request.POST["password"],
            "confirm_password" : request.POST["confirm_password"],
        }
        
        new_user = User.objects.create_user(user_details["username"],user_details["email_address"],user_details["password"])
        new_user.first_name = user_details["first_name"]
        new_user.last_name = user_details["last_name"]
        
        new_user.save()
        messages.success(request,"Your Account is Created")
        return redirect("signin")
        
    return render(request,"authentication/signup.html")

#------------------------------------------------------------------------

def signin(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username,password=password)
        
        
        if user is not None: #if user added right Credentials redirect user to root path again
            login(request,user)
            print("ok")
            return redirect("home")
        else: #rediect him signin page with error messages
            messages.error(request,"bad Credentials")
            return redirect("signin")
            
        
    return render(request,"authentication/signin.html")


#------------------------------------------------------------------------

def signout(request):
    logout(request)
    return redirect("home")
    