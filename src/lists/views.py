from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
import json
from tmdbv3api import TMDb,Movie
import os

tmdb = TMDb()
tmdb.api_key = os.environ.get("TMDB_API_KEY")
tmdb.language = 'en'
tmdb.debug = True



# Create your views here.
def showlists(request,username):
    user = User.objects.filter(username=username)
    if user:
        lists = []
        for list in user[0].lists.all():
            poster = []
            count = 0
            for movie in list.movies.all():
                if count >= 5:
                    break
                poster.append(movie.poster_path)
                count += 1
            if count < 5:
                for i in range(5-count):
                    poster.append("")

            lists.append({
                "list": list,
                "posters": poster,
            });
        context = {
            "search_user":user[0],
             "user_lists": user[0].lists.all(),
             "lists":lists,
        }
        return render(request,"lists/list_page.html",context=context)
    return render(request,"profile_page/error.html")

def showlist(request,username,listid):
    search_user = User.objects.filter(username=username)
    if search_user:
        list = search_user[0].lists.filter(id=listid)
        list_present = False
        if list:
            list_present = True

        if list_present:
            m = Movie().details(list[0].movies.all()[0].tmdb_id).backdrop_path
            
            context = {
                "the_user": search_user[0],
                "list": list[0],
                "backdrop_path":m,
            }
            return render(request,"lists/a_list.html",context=context)

    return render(request,"main/error.html")




def newlist(request):
    context = {
        "page_type":"newlist",
    }
    response =  render(request,"lists/new_list.html",context=context)
    response.set_cookie(key="username",value=request.user.username)
    return response


def editlist(request,listid):
    list = request.user.lists.get(id=listid)
    if list:
        context = {
        "page_type":"editlist",
        "user_list":list,
        }
        return render(request,"lists/new_list.html",context=context)
    return render(request,"main/error.html")



    


def postlist(request):
    if request.method == "POST":
        data = json.load(request)
        user_list = request.user.profile.addList(data[0],data[1:])
        response ={"message":"sucessfull","message":"list Created","id":user_list.id}
        return HttpResponse(json.dumps(response),content_type='application/json')
    return render(request,"main/error.html")


def updatelist(request):
    if request.method == "POST":
        data = json.load(request)
        response ={"message":"sucessfull","message":"list updated"}
        request.user.profile.updateList(data[0],data[1:])
        return HttpResponse(json.dumps(response),content_type="application/json")
    return render(request,"main/error.html")



def add_movie(request):
    if request.method == "POST":
        data = json.load(request)
        user_list = request.user.profile.add_into_list(data["movie_id"],data["list_id"])
        response = {
            "status":"success",
            "message":f"movie added in {user_list.name}"
        }
        return HttpResponse(json.dumps(response),content_type="application/json")

    return render("main/error.html")




