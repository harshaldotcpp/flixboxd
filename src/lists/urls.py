from django.urls import path,include
from . import views

app_name = "list"

urlpatterns = [
    path('new',views.newlist,name="newlist"),
    path('post',views.postlist,name="postlist"),
    path('<str:username>',views.showlists,name="showlists"),
]