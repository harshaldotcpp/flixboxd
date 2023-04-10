from django.shortcuts import render
from django.contrib.auth.models import  User
from django.http import JsonResponse,HttpResponse
import json
# Create your views here.

def user_profile(request,username):
    info = {
        "username":username
    }

    user = User.objects.filter(username=username)

    if user:
        info["user_profile"] = user[0]
        response =  render(request,"profile_page/profile.html",context=info)
        response.set_cookie(key="username",value=username)
        return response

    return render(request,"profile_page/error.html",context=info) 


def follow_user(request,username):
    if request.method == "POST":
        req = json.load(request)
        follow = req["follow"]
        response_data = {
            "status": "succesfull",
            "message": f"unfollowed {username}"
        }

        if follow:
            response_data['message'] =  f"following {username}"
            request.user.profile.follow_user(username)
            return HttpResponse(json.dumps(response_data),content_type='application/json') 

        request.user.profile.unfollow_user(username)
        return HttpResponse(json.dumps(response_data),content_type='application/json') 


def settings(request):
    print(dir(request.user))
    return render(request,"profile_page/settings.html")