from pathlib import Path

def count_words(filename, word):
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, I can't find {filename}.")
    else: 
        number = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {number} times."
        print(msg)

count_words('learning_python.txt', 'you')
count_words('alice.txt', 'the')
count_words('alice.txt', 'the ')