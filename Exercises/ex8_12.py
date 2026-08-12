def sandwich_toppings(*toppings):
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

sandwich_toppings('beef')
sandwich_toppings('beef', 'chicken')
sandwich_toppings('beef', 'chicken', 'tuna')