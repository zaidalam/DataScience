# For Loops
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(number)

# For Loops with append
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = []
for number in numbers:
    if number % 2 == 0:
        print(number)
        even_number.append(number)


