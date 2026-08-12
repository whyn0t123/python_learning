import json
from pathlib import Path

number = input("Enter yout favourite number: ")

path = Path('numbers.json')
contents = json.dumps(number)
path.write_text(contents)

print("Thanks! I'll remember that number.")