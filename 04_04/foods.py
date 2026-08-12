my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

print("The last three items in the list are:")
for food in my_foods[-3:]:
    print(food)