from django.db import models
from django.contrib.auth.models import User
from films.models import Film
# Create your models here.



class List(models.Model):
    name = models.CharField(max_length=500)
    movies = models.ManyToManyField(Film)
    user = models.ForeignKey(User,related_name="lists",on_delete=models.CASCADE) 
    liked_by = models.ManyToManyField(User,related_name="liked_list_set")
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    update_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.user.username}"