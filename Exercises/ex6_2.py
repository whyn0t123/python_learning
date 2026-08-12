favourite_numbers = {
    'a': [1,6],
    'b': [2,7],
    'c': [3,8],
    'd': [4,9],
    'e': [5,10],
}

for name, numbers in favourite_numbers.items():
    print(f"{name.title()}:")
    for number in numbers:
        print(number)