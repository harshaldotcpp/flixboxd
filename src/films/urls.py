from django.contrib import admin
from django.urls import path
from . import views

app_name = "films"
urlpatterns = [
    path('',views.film,name="film"),
    path('watchedadd',views.watched, name="watched"),
    path('likedadd',views.liked,name="liked"),
    path('watchlistadd',views.watchlist,name="watchlist"),
    path('film/<str:film_name>',views.search_films,name="search_films"),
]