from django import template
from films.models import WatchedMovie,Watchlist
import calendar

register = template.Library()

@register.simple_tag
def is_liked(movie,username,true,false):
    if movie.liked_by.filter(username=username).exists():
        return true
    return false 

@register.simple_tag
def is_watched(movie,username):
    if movie.watched_by.filter(username=username).exists():
        return ""
    return "hidden"


@register.simple_tag
def is_watched_tmdb(tmdb_id,user,true,false):
    if user.movies_set.filter(tmdb_id=tmdb_id):
        return true
    
    return false



@register.simple_tag
def is_liked_tmdb(tmdb_id,user,true,false):
    if user.liked_movies_set.filter(tmdb_id = tmdb_id):
        return true
    return false


@register.simple_tag
def is_watchlist_tmdb(tmdb_id,user,true,false):
    if user.watchlist_set.filter(tmdb_id=tmdb_id):
        return true
    return false

@register.simple_tag
def what_rated(user,tmdb_id,star):
    movie = user.movies_set.filter(tmdb_id = tmdb_id)
    if movie:
        rating = user.rating_set.filter(movie=movie[0])
        if rating and rating[0].stars == star:
            return "checked"
    return "unchecked"



@register.simple_tag
def get_month_name(number):
    return calendar.month_abbr[number]


def get_rating(user,tmdb_id):
    movie = user.movies_set.filter(tmdb_id = tmdb_id)
    if movie:
        rating = user.rating_set.filter(movie=movie[0])
        if rating:
            return  rating[0].stars 
    return 0 





@register.simple_tag
def rating_to_stars(user,tmdb_id):
    rating = get_rating(user,tmdb_id) 
    star = {
        0:[""],
        0.5:["◐"],
        1:["●"],
        1.5:["●","◐"],
        2:["●","●"],
        2.5:["●","●","◐"],
        3:["●","●","●"],
        3.5:["●","●","●","◐"],
        4:["●","●","●","●"],
        4.5:["●","●","●","●","◐"],
        5:["●","●","●","●","●"],
    }

    return star[rating]


@register.simple_tag
def isNewMonth(current_month,new_month,true,false):
    if current_month != new_month:
        return true
    return false


@register.simple_tag
def updateNewMonth(current_month,new_month):
    if current_month != new_month:
        return current_month
    return new_month