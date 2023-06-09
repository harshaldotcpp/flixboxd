from django.urls import path,include
from . import views

app_name = "list"

urlpatterns = [
    path('new',views.newlist,name="newlist"),
    path('post',views.postlist,name="postlist"),
    path('update',views.updatelist,name="updatelist"),
    path('addmovie',views.add_movie,name="addmovie"),
    path('delete',views.delete,name="delete_list"),
    path('edit/<int:listid>',views.editlist,name="editlist"),
    path('<str:username>',views.showlists,name="showlists"),
    path('<str:username>/<int:listid>',views.showlist,name="showlist"),
]