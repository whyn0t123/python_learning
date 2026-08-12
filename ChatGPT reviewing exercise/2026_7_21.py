from pathlib import Path
path = Path('users.txt')

users = []

while True:
    print("Enter 'q' if you want to quit the program.")

    name = input("Enter your name: ")

    if name == 'q':
        break
    
    while True:
        age = input("Enter your age: ")

        if age.isdigit():
            age = int(age)
            break

        else:
            print("Please enter a number.")

    if age == 'q':
            break
    
    language = input("Enter your favourite language: ")
    if language == 'q':
        break
    
    user = {'name': name, 'age': age, 'language': language}

    users.append(user)

contents = ""

for user in users:
    for key, value in user.items():
        print(f"{key}: {value}")
        contents += f"{key}: {value}\n"
        
    print("----------------")
    contents += "----------------\n"
        
path.write_text(contents)