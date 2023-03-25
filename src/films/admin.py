from django.contrib import admin
from .models import WatchedMovie,Watchlist
# Register your models here.


admin.site.register([WatchedMovie,Watchlist])