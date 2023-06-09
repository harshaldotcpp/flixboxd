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
    path('getavgstars',views.avgStars,name="avgStars"),
    path('directlogged',views.directLogged,name="directLogged"),
    path('actor/<int:id>',views.actor,name="actor"),
    path('watched/<str:username>',views.showWatched,name="showWatched"),
    path('watchlist/<str:username>',views.showWatchlist,name="showWatchlist"),
    path('diary/<str:username>',views.diary ,name="diary"),
    path('search/<str:film_name>',views.search_films,name="search_films"),
    path('isliked/<int:film_id>',views.isLiked,name="isLiked"),
    path('getstars/<int:film_id>',views.getStars,name="getStars")
]