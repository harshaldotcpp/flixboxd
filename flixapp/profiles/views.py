from django.shortcuts import render

# Create your views here.

def user_profile(request,username):
    print(username)
    print("profile page")
    return render(request,"profile_page/profile.html",{"username":username})
