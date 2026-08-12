info_0 = {'first_name': 'Jinping', 'last_name': 'Xi', 'age': 73, 'city': 'Beijing'}
info_1 = {'first_name': 'xiaoping', 'last_name': 'deng', 'age': 83, 'city': 'shanghai'}
info_2 = {'first_name': 'zedong', 'last_name': 'mao', 'age': 93, 'city': 'changsha'}

people = [info_0, info_1, info_2]

for info in people:
    first = info['first_name']
    last = info['last_name']
    age = info['age']
    city = info['city']
    
    full_name = f"{first} {last}"
    print(f"Full name: {full_name.title()}")
    print(f"Age:{age}")
    print(f"City: {city}")