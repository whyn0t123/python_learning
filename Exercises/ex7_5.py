active = True

while active:
    age = input("How old are you? ")
    age = int(age)
    if age < 3:
        print("free.")
        active = False
    elif age < 12:
        print("$10.")
        active = False
    else:
        print("$15.")
        active = False