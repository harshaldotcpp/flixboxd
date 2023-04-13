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
            count = 0
            if 5 - list.movies.count() > 1:
                count = 5 - list.movies.count()

            lists.append({
                "list": list,
                "range": [i for i in range(count)],
            });
        context = {
            "search_user":user[0],
             "user_lists": user[0].lists.all(),
             "lists":lists,
        }
        return render(request,"lists/list_page.html",context=context)
    return render(request,"profile_page/error.html")

def newlist(request):
    return render(request,"lists/new_list.html")


def postlist(request):
    if request.method == "POST":
        data = json.load(request)
        request.user.profile.addList(data[0],data[1:])
        response ={"success":"succefull","message":"yes post request"}
        return HttpResponse(json.dumps(response),content_type='application/json')
    return render(request,"main/error.html")