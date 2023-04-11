from django.urls import path,include
from . import views

app_name = "list"

urlpatterns = [
    path('<str:username>',views.showlists,name="showlists"),
    path('',views.newlist,name="newlist")
]