from django.contrib import admin
from .models import Rating,DiaryLog,Film
# Register your models here.


admin.site.register([Rating,DiaryLog,Film])