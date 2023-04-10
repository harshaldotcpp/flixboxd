from django.shortcuts import render
from django.contrib.auth.models import  User
from django.http import JsonResponse,HttpResponse
from django.shortcuts import redirect
from .utilities import validatePayload
from django.contrib import messages
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
    return render(request,"profile_page/settings.html")

def settingsUpdate(request):
    if request.method == "POST":
        payload = {
        #"username":  request.POST['username'],
        "first_name": request.POST['first_name'],
        "last_name" : request.POST['last_name'],
        #"email" : request.POST['email'],
        "bio" : request.POST['bio'],
        "pfp":  "",
        }
        if(request.FILES.get('pfp',False)):
            payload['pfp'] = request.FILES['pfp']
        
        payload = validatePayload(request.user, payload)
        request.user.first_name = payload['first_name'] 
        request.user.last_name = payload['last_name'] 
        request.user.profile.bio = payload['bio']
        request.user.profile.profile_picture = payload['pfp']
        request.user.save()
        messages.success(request,"Profile Updated!")        
        return redirect("/profile/settings")

    return render(request,"profie_page/error.html")