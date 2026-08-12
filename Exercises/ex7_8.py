sandwich_orders = ['tuna', 'ham', 'beef', 'pastrami', 'pastrami', 'chicken', 'pastrami']
finished_sandwiches = []

print("The pastrami has sold out.\n")

while  'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop(0)
    print(f"I made your {current_sandwiches} sandwich.")
    finished_sandwiches.append(current_sandwiches)

print("\nFinished sandwiches:")

for sandwich in finished_sandwiches:
    print(sandwich)