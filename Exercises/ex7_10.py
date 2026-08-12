responses = {}

prompt_0 = "\nIf you could visit one place in the world, where would you go?"
prompt_1 = "\nWould you like to let another person respond? (yes/no) "

polling_active = True

while polling_active:
    name = input("What's your name?")
    response = input(prompt_0)
    responses[name] = response
    repeat = input(prompt_1)
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(f"{name.title()} would go to {response.title()}.")