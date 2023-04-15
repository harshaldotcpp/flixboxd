from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from profiles.views import user_profile



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("authentication.urls")),
    path('film/',include("films.urls")),
    path('lists/',include("lists.urls")),
    path('<str:username>',include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
