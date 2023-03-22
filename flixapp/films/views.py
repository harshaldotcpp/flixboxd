from django.shortcuts import render

# Create your views here.


def film(request,film_name):
    info = {
        "film_name":film_name,
    }
    return render(request,"film/film.html",info)