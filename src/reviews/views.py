from django.shortcuts import render
from django.contrib.auth.models import User
from . models import Review
import json
# Create your views here.
def reviews(reqeust,username):
    user = User.objects.filter(username=username)
    if user:
        likes = "No like yet"
        context = {
            "search_user": user[0] ,
            "reviews": user[0].reviews_set.order_by("-date"),
        }
        return render(reqeust,"reviews/reviews_page.html",context=context)
    return render(reqeust,"main/error.html")

def like(reqeust):
    if reqeust.method == "POST":
        data = json.load(reqeust)
        if data["addlike"]:
            Review.like(data["username"],data["review_id"])
        else:
            Review.unlike(data["username"],data["review_id"])

    return render(reqeust,"main/error.html")