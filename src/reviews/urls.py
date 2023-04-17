from django.urls import path,include
from . import views



urlpatterns = [
    path("",views.reviews,name="user_reviews"),
    path("",views.reviews,name="user_reviews")
]

