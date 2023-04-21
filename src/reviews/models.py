from films.models import Film
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    review = models.CharField(max_length=1000)
    movie = models.ForeignKey(Film,on_delete=models.CASCADE,related_name="reviews_set")
    date = models.DateTimeField(auto_now_add=True)
    review_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews_set")
    liked_by = models.ManyToManyField(User,related_name="liked_review_set")
    review_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"review:{ self.review},movie:{self.movie.original_title}"

    def like(username,review_id):
        user = User.objects.get(username=username)
        review = Review.objects.get(id=review_id)
        review.liked_by.add(user)
        review.likes_count += 1
        review.save()

    def unlike(username,review_id):
        user = User.objects.get(username=username)
        review = Review.objects.get(id=review_id)
        review.liked_by.remove(user)
        review.likes_count -= 1
        review.save()
        