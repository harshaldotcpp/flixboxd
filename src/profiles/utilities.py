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
