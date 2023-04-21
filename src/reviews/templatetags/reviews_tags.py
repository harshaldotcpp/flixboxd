from django import template
register = template.Library()


@register.simple_tag
def is_review_liked(user,review,true,false):
    if review.liked_by.filter(username=user.username).exists():
        return true
    return false