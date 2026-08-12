from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nEnter your name: "
prompt += "\nEnter 'quit' if you are the last guest."

guest_names = []

while True:
    name = input(prompt)
    if name == 'quit':
        break
    
    guest_names.append(name)

file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)