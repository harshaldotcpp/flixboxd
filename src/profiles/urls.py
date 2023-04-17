from django.urls import path,include
from . import views

app_name = "profiles"

urlpatterns = [
    path('',views.user_profile,name="user_profile"),
    path('/reviews',include("reviews.urls")),
    path('/following',views.following,name='followings'),
    path('/followers',views.followers,name='followers'),
    path('/settings',views.settings,name="settings"),
    path('/update',views.settingsUpdate,name="settingUpdate"),
    path('/updatetop',views.updatetop,name="updatetop"),
    path('/follow/<str:username>',views.follow_user,name="follow_user"),
]