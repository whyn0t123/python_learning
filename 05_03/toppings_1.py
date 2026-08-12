requested_toppings=['mushrooms','extra cheese','green pepper']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.\n")

for requested_topping in requested_toppings:
    if requested_topping == 'green pepper': 
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("Finishing making your pizza!\n")

requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinishing making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#5.4.3
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','fresh fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we are out of {requested_topping} right now.")

print("\nFinishing making your pizza!")       