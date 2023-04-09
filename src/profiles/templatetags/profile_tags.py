from django import template
from django.contrib.auth.models import User
from films.models import WatchedMovie,Watchlist
import datetime

register = template.Library()

@register.simple_tag
def films_watched_count(username):
    user = User.objects.get(username=username)
    return user.movies_set.count()

@register.simple_tag
def get_following_count(username):
    user = User.objects.get(username=username)
    return user.profile.following.count()

@register.simple_tag
def get_followers_count(username):
    user = User.objects.get(username=username)
    return user.profile.followers.count()


@register.simple_tag
def get_lists_count(username):
    user = User.objects.get(username=username)
    return user.list_set.count()

@register.simple_tag
def is_following(follower,username,true,false):
    user = User.objects.get(username=username)
    if follower.profile.following.filter(user=user):
        return true 
    return false 


@register.simple_tag
def is_following_tag(follower,username):
    user = User.objects.get(username=username)
    if follower.profile.following.filter(user=user):
        return "unfollow"
    return "follow"
    
    
@register.simple_tag
def get_year_films_count(user):
    current_year = datetime.datetime.today().year
    print(current_year)
    return  user.diary_log.filter(date__year=current_year).count()