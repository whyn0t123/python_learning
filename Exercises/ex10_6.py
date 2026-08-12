print("Give me two numbers, and I will add them.")
print("Enter 'q' to quit.")

while True:
    try:
        first_number = input("First number: ")

        if first_number == 'q':
            break
        first_number = int(first_number)

        second_number = input("Second number: ")

        if second_number == 'q':
            break
        second_number = int(second_number)

    except ValueError:
        print("Please enter a number.")
        
    else:
        sum = first_number + second_number
        print(f"The sum of {first_number} and {second_number} is {sum}.")