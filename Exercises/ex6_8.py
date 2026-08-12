pet_0 = {'type': 'cat', 'lord': 'a'}
pet_1 = {'type': 'dog', 'lord': 'b'}
pet_2 = {'type': 'bird', 'lord': 'c'}

pets = [pet_0, pet_1, pet_2]
 
for pet in pets:
    type = pet['type']
    lord = pet['lord']
    print(f"\nType:{type}")
    print(f"Lord:{lord}")