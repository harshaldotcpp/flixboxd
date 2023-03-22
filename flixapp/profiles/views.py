from django.shortcuts import render

# Create your views here.

def user_profile(request,username):
    print(username)
    info = {
        "username":username
    }
    return render(request,"profile_page/profile.html",info)

