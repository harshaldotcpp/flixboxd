from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import WatchedMovie
from .models import Watchlist


@receiver(m2m_changed,sender=WatchedMovie.watched_by.through)
def remove_operation(sender,instance,action,**kwargs):
    if action == "post_add":
        print(instance.username)
  
