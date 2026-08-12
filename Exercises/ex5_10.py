current_users = ['A','b','c','D','e']
new_users = ['a','B','f','g','h']
current_users_lower = [current_user.lower() for current_user in current_users]
new_users_lower = [new_user.lower() for new_user in new_users]
for new_user_lower in new_users_lower:
    if new_user_lower in current_users_lower:
        print("This name has been used.")
    else:
        print("OK")