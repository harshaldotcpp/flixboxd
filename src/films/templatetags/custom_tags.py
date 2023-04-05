from django import template
from films.models import WatchedMovie,Watchlist

register = template.Library()

@register.simple_tag
def is_liked(movie,username):
    if movie.liked_by.filter(username=username).exists():
        return ""
    return "hidden" 

@register.simple_tag
def is_watched(movie,username):
    if movie.watched_by.filter(username=username).exists():
        return ""
    return "hidden"


@register.simple_tag
def is_watched_tmdb(tmdb_id,username):
    movie = WatchedMovie.objects.filter(tmdb_id=tmdb_id)

    if movie:
        if movie[0].watched_by.filter(username=username):
            return ""
    return "hidden"


@register.simple_tag
def is_liked_tmdb(tmdb_id,username):
    movie = WatchedMovie.objects.filter(tmdb_id=tmdb_id)
    if movie:
        if movie[0].liked_by.filter(username=username):
            return ""
    return "hidden"


@register.simple_tag
def is_watchlist_tmdb(tmdb_id,username):
    movie = Watchlist.objects.filter(tmdb_id = tmdb_id) 
    if movie:
        if movie[0].watch_listed.filter(username=username):
            return ""
    return "hidden"