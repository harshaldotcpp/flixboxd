from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def reviews(reqeust,username):
    user = User.objects.filter(username=username)
    print(user[0].username)
    if user:
        likes = "No like yet"
        context = {
            "search_user": user[0] ,
            "reviews": user[0].reviews_set.order_by("-date"),
        }
        return render(reqeust,"reviews/reviews_page.html",context=context)
    return render(reqeust,"main/error.html")