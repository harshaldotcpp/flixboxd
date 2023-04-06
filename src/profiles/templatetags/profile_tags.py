from django import template
from django.contrib.auth.models import User
from films.models import WatchedMovie,Watchlist

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
def is_following(follower,username):
    user = User.objects.get(username=username)
    if follower.profile.following.filter(user=user):
        return "checked"
    return "unchecked"


@register.simple_tag
def is_following_tag(follower,username):
    user = User.objects.get(username=username)
    if follower.profile.following.filter(user=user):
        return "unfollow"
    return "follow"
    
    