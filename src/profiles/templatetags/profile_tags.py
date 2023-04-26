from django import template
from django.contrib.auth.models import User
import datetime
from django.templatetags.static import static

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
    return user.lists.count()

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


@register.simple_tag
def checkTop(pos,true,false):
    if pos == None:
        return false
    return true

@register.simple_tag
def topImage(pos,res):
    if pos == None:
        return static('main/image/defaultposter.png')
    url = f"https://image.tmdb.org/t/p/{res}" + pos.poster_path
    return url



@register.simple_tag
def isnone(obj):
    if obj == None:
        return "true"
    return "false"


@register.simple_tag
def get_tmdb_id(top):
    if top:
        return top.tmdb_id
    return None


@register.simple_tag
def get_poster_path(top):
    if top:
        return top.poster_path
    return None




@register.simple_tag
def topPosterPath(top):
    if top:
        return "https://image.tmdb.org/t/p/w200" + top.poster_path
    return static("main/image/defaultposter.png")


@register.simple_tag
def topTmdb_id(top):
    if top:
        return top.tmdb_id
    return 0