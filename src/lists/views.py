from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def showlists(request,username):
    user = User.objects.filter(username=username)
    if user:
        context = {
            "search_user":user[0],
        }
        return render(request,"lists/list_page.html",context=context)
    return render(request,"profile_page/error.html")

def newlist(request):
    return render(request,"lists/new_list.html")