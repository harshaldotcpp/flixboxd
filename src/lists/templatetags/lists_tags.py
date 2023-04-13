from django import template
from django.templatetags.static import static


register = template.Library()

@register.simple_tag
def subtract(value,mid, arg):
    print(value,arg)
    res = value - (mid* arg)
    return str(res)