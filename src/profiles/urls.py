from django.urls import path,include
from . import views

app_name = "profiles"

urlpatterns = [
    path('',views.user_profile,name="user_profile"),
    path('follow/<str:username>',views.follow_user,name="follow_user"),
    path('settings',views.settings,name="settings"),
    path('update',views.settingsUpdate,name="settingUpdate")
]