from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import WatchedMovie
from .models import Watchlist


@receiver(m2m_changed,sender=WatchedMovie.watched_by.through)
def remove_operation(sender,instance,action,**kwargs):
    if action == "post_add":
        user = instance.watched_by.through.objects.last().user
  
        movie = user.watchlist_set.filter(tmdb_id = instance.tmdb_id)
        if movie:
            user.watchlist_set.remove(movie[0])
