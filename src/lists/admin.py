from django.contrib import admin
from .models import List,ListMovie, Note
# Register your models here.

admin.site.register([List,ListMovie,Note])