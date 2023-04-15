from django.contrib import admin
from .models import WatchedMovie,Rating,DiaryLog,Film
# Register your models here.


admin.site.register([WatchedMovie,Rating,DiaryLog,Film])