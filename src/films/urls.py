from django.contrib import admin
from django.urls import path
from . import views

app_name = "filmsabout"
urlpatterns = [
    path('<int:film_id>',views.film,name="film"),
    path('watchedadd',views.watched, name="watched"),
    path('likedadd',views.liked,name="liked"),
    path('watchlistadd',views.watchlist,name="watchlist"),
    path('reviewadd',views.addReview,name="addReview"),
    path('ratingadd',views.rating,name="ratingadd"),
    path('ratingremove',views.removeRating,name="removeRating"),
    path('watched/<str:username>',views.showWatched,name="showWatched"),
    path('watchlist/<str:username>',views.showWatchlist,name="showWatchlist"),
    path('film/<str:film_name>',views.search_films,name="search_films"),
]