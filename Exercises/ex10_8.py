from pathlib import Path

def read_file(filename):
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, I can't find {filename}.")
    else:        
        print(f"\nReading file:{filename}")
        print(contents)

read_file('cats.txt')
read_file('dogs.txt')