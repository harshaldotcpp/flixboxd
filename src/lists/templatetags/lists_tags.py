from django import template
from django.templatetags.static import static


register = template.Library()

@register.simple_tag
def subtract(value,mid, arg):
    list = ["z-50","z-40","z-30","z-20","z-10",'z-0']
    res = value - (mid* arg)
    return str(res)



@register.simple_tag
def checkPoster(poster,w):
    if poster == "":
        return static("main/image/defaultposter.png")
    return f"https://image.tmdb.org/t/p/{w}/" + poster