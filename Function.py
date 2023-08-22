import json

def get_data_user():
    with open('user.json', 'r',  encoding='utf-8') as f:
        user = json.load(f)
    return user

def register(user_name, passw, user):
    if user_name not in user:
        user[user_name] = passw
        with open('user.json', 'w') as f:
            json.dump(user, f)
        return True
    else:
        return False
