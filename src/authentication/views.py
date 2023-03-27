from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
   
  
    if request.user.is_authenticated: #if user is already is_authenticated(looged in) then take user to home page
        return render(request,"main/home.html")
   
   #else user will to welcome page
    return render(request,"authentication/index.html")
    
    
#------------------------------------------------------------------------

def signup(request):
    if request.method == "POST":
        print(request.POST)
        user_details = {
            "username" : request.POST["username"],
            "first_name" : request.POST["first_name"],
            "last_name" : request.POST["last_name"],
            "email_address" : request.POST["email_address"],
            "password" : request.POST["password"],
            "confirm_password" : request.POST["confirm_password"],
        }
        
        if User.objects.filter(username=user_details["username"]):
            print("heelo1")
            messages.error(request,"username already exist!")
            return redirect ("authentication:signup")
            
        if User.objects.filter(email=user_details["email_address"]):
            messages.error(request,"Email Already Registered")
            print("hello2")
            return redirect("authentication:signup")
        
        new_user = User.objects.create_user(user_details["username"],user_details["email_address"],user_details["password"])
        new_user.first_name = user_details["first_name"]
        new_user.last_name = user_details["last_name"]
        
        new_user.save()
        user = authenticate(username=user_details["username"], password=user_details["password"])
        login(request,user)
        messages.success(request,"Your Account is Created")
        print("hello3")
        return redirect("authentication:home")
        
    print("hello")
    return render(request,"authentication/index.html")

#------------------------------------------------------------------------

def signin(request):
   
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username,password=password)
        
        
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
    