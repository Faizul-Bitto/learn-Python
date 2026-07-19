double = [x * 2 for x in range(1, 11)]

triple = [x * 3 for x in range(1, 11)]

print(triple)
print()

fruits = [
    "apple",
    "orange",
    "banana",
]

fruits = [fruit.upper() for fruit in fruits]
print(fruits)
print()

numbers = [1, -2, 3, -4, 5, -6]
positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)
