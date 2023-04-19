from django.shortcuts import render
from django.contrib.auth.models import  User
from django.http import JsonResponse,HttpResponse
from django.shortcuts import redirect
from .utilities import validatePayload,addInTopFour,noFavroite
from django.contrib import messages
import json

# Create your views here.
#shows profile page
def user_profile(request,username):
    
    info = {
        "username":username,
    }
    user = User.objects.filter(username=username)

    if user:
        info["user_profile"] = user[0]
        info["watchlist"] = user[0].watchlist.all()[:4]
        info["top4"] = user[0].top4
        info["recent_log"] = user[0].diary_log.order_by("-date","-created_at")[:4]
        info["recent_log_len"] = len(user[0].diary_log.order_by("-date","-created_at")[:4])
        info["reviews"] = user[0].reviews_set.order_by("-date")[:2]
        favs = False
        if noFavroite(info["top4"]):
            favs = True 
        info["favs"] = favs
        response =  render(request,"profile_page/profile.html",context=info)
        response.set_cookie(key="profile_username",value=username)
        response.set_cookie(key="username",value=request.user.username)
        return response

    return render(request,"profile_page/error.html",context=info) 

#need login (ajax request)
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

#need login
def settings(request,username):
    if username != request.user.username:
        return render(request,"main/error.html")
    context = {
         "top4": request.user.top4,
         "user": request.user,
    }
    response = render(request,"profile_page/settings.html")
    response.set_cookie("username",request.user.username)
    return response

#need login
def settingsUpdate(request,username):
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
        return redirect(f"/{request.user.username}/settings")

    return render(request,"profie_page/error.html")


#login need (ajax request)
def updatetop(request,username):
    if request.method == "POST" or request.user.username == username:
        top4 = json.load(request)
        addInTopFour(request.user,top4[0],"one")
        addInTopFour(request.user,top4[1],"two")
        addInTopFour(request.user,top4[2],"three")
        addInTopFour(request.user,top4[3],"four")
        response_data = {
            "status": "succesfull",
            "message": "Top List Updated",
        }
        return HttpResponse(json.dumps(response_data),content_type='application/json') 

    return render(request,"profile_page/error.html")

def following(request,username):
    search_user = User.objects.filter(username=username)
    context = {"page_type":"following"}
    if search_user:
        context["search_user"] = search_user[0]
        context['followings'] = search_user[0].profile.following.all()
        print(context["followings"])
        
        return render(request,"profile_page/following.html",context=context)
    return render(request,"profile_page/error.html")


def followers(request,username):
    search_user = User.objects.filter(username=username)
    context = {"page_type":"followers"}
    if search_user:
        context["search_user"] = search_user[0]
        context["followers"] = search_user[0].profile.followers.all()
        return render(request,"profile_page/followers.html",context=context)
    return render(request,"profile_page/error.html")

def search(request,username):
    context = {
        "searched_users":User.objects.filter(username__startswith=username),
        "search_value":username,
        "btn_color":"text-blue-300",
    }
    print(context["searched_users"])
    return render(request, "profile_page/search_profile.html",context=context) 