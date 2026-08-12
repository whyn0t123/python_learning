def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile_0 = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile_0)

user_profile_1 = build_profile('Zhiyuan', 'Nie', 
                               location='Guangzhou',
                               field='cs',
                               hobby='cs')
print(user_profile_1)