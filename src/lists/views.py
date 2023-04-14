from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
import json

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

def newlist(request):
    context = {
        "page_type":"newlist",
    }
    return render(request,"lists/new_list.html",context=context)


def editlist(request,listid):
    list = request.user.lists.filter(id=listid)
    if list:
        context = {
        "page_type":"editlist",
        "user_list":list[0],
        }
        return render(request,"lists/new_list.html",context=context)
    return render(request,"main/error.html")



    


def postlist(request):
    if request.method == "POST":
        data = json.load(request)
        request.user.profile.addList(data[0],data[1:])
        response ={"message":"sucessfull","message":"list Created"}
        return HttpResponse(json.dumps(response),content_type='application/json')
    return render(request,"main/error.html")


def updatelist(request):
    if request.method == "POST":
        data = json.load(request)
        response ={"message":"sucessfull","message":"list Created"}
        request.user.profile.updateList(data[0],data[1:])
        return HttpResponse(json.dumps(response),content_type="application/json")
    return render(request,"main/error.html")