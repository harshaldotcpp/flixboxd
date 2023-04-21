from django.urls import path,include
from . import views



urlpatterns = [
    path("",views.reviews,name="user_reviews"),
    path("like",views.like,name="user_reviews")
]

