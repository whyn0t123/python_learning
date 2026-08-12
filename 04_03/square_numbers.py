#方法一
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
#方法二
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)
#方法三
squares = [value ** 2 for value in range(1,11)]
print(squares)