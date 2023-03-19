numbers = [1, 2, 3, 4]
numbers_v2 = []

for n in numbers:
    numbers_v2.append(n * 2)

numbers_v3 = list(map(lambda x: x * 2, numbers))

print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
numbers_3 = list(map(lambda x, y: x + y, numbers_1, numbers_2))

print(numbers_3)
