pizzas=['pizza a','pizza b', 'pizza c']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza}.")
print("I really love pizza!")             

friend_pizzas=pizzas[:]
pizzas.append('pizza d')
friend_pizzas.append('pizza e')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friends favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)