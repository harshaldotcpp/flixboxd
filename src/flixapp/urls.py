from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


app_name = "flixapp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("authentication.urls")),
    path('<str:username>',include("profiles.urls")),
    path('film/',include("films.urls")),
    path('search/',include("films.urls")),
    path('profile/',include('profiles.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
