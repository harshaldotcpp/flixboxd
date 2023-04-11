from .models import Top4Movies

def validatePayload(user,payload):
    # if payload["username"] == '':
    #     payload["username"] = user.username

    if payload["first_name"] == '':
        payload["first_name"] = user.first_name

    if payload['last_name'] == '':
        payload['last_name'] = user.last_name

    # if payload['email'] == '':
    #     payload['email'] = user.email

    if payload["pfp"] == '':
        payload['pfp'] = user.profile.profile_picture
    
    return payload


def addInTopFour(user,top,pos):
    if pos == "one":
        if top["is_present"]:
            m = Top4Movies.objects.filter(tmdb_id = top["id"])
            if m:
                user.top4.one = m[0]
                user.top4.save()
                return
            new_topm = Top4Movies.objects.create(tmdb_id = top["id"],poster_path=top["poster_path"])
            new_topm.save()
            user.top4.one = new_topm
            user.top4.save()
            return
        else:
            user.top4.one = None
            user.top4.save()

    if pos == "two":
        if top["is_present"]:
            m = Top4Movies.objects.filter(tmdb_id = top["id"])
            if m:
                user.top4.two = m[0]
                user.top4.save()
                return
            new_topm = Top4Movies.objects.create(tmdb_id = top["id"],poster_path=top["poster_path"])
            new_topm.save()
            user.top4.two = new_topm
            user.top4.save()
            return
        else:
            user.top4.two = None
            user.top4.save()
            
    if pos == "three":
        if top["is_present"]:
            m = Top4Movies.objects.filter(tmdb_id = top['id'])
            if m:
                user.top4.three = m[0]
                user.top4.save()
                return
            new_topm = Top4Movies.objects.create(tmdb_id = top['id'],poster_path=top['poster_path'])
            new_topm.save()
            user.top4.three = new_topm
            user.top4.save()
            return
        else:
            user.top4.three = None
            user.top4.save()

    if pos == "four":
        if top["is_present"]:
            m = Top4Movies.objects.filter(tmdb_id = top['id'])
            if m:
                user.top4.four = m[0]
                user.top4.save()
                return
            new_topm = Top4Movies.objects.create(tmdb_id = top['id'],poster_path=top['poster_path'])
            new_topm.save()
            user.top4.four = new_topm
            user.top4.save()
            return
        else:
            user.top4.four = None
            user.top4.save()
    return





