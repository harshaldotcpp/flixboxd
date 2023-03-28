from django.contrib import admin
from .models import WatchedMovie,Watchlist,Rating,DiaryLog,List
# Register your models here.


admin.site.register([WatchedMovie,Watchlist,Rating,DiaryLog,List])