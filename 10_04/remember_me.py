from pathlib import Path
import json

def greet_user():
    path = Path('user_dict.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        correct = input(f"Are you {user_dict['username']}?(y/n)")
        if correct == 'y':
            print(f"Welcome back, {user_dict['username']}!")
            print(f"Hope you've been playing some {user_dict['game']}.")
            print(f"Have you seen a {user_dict['animal']} recently?")
        else:
            user_dict = get_new_user_info(path)
            print(f"We'll remember you when you come back, {user_dict['username']}!")
    else:
        user_dict = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_dict['username']}!")

def get_stored_user_info(path):
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None
    
def get_new_user_info(path):
    username = input("What's your name?")
    game = input("What's your favourite game?")
    animal = input("What's your favourite animal?")

    user_dict = {'username':username, 'game':game, 'animal':animal}

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

greet_user()