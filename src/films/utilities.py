def get_friends_watched_film(user,film):
    friends = user.profile.following.all()
    f_usernames = []
    for friend in friends:
        f_usernames.append(friend.user.username)
    watched_by = film.watched_by.all().filter(username__in = f_usernames)
    friends_watched = []
    for watched in watched_by:
        if watched.rating_set.filter(movie=film).exists():
            friends_watched.append({"friend":watched,"rating":watched.rating_set.get(movie=film).stars})
        else:
            friends_watched.append({"friend":watched,"rating": 0})

    return friends_watched


def get_friends_watchedlisted_film(user,film,watched):
    friends = user.profile.following.all()
    f_usernames = []
    for friend in friends:
        if not film.watched_by.filter(username = friend.user.username).exists():
            f_usernames.append(friend.user.username)
    watched_by = film.watchlisted_by.all().filter(username__in = f_usernames)
    return watched_by
 




