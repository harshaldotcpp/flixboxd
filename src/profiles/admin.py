from django.contrib import admin
from .models import Profile, Top4,Top4Movies

# Register your models here.


admin.site.register([Profile,Top4,Top4Movies])
