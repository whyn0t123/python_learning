from pathlib import Path
import json

path = Path('number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("Enter your favourite number: ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks! I'll remember that number.")
else:
    number = json.loads(contents)
    print(f"I know your favourite number! It's {number}.")