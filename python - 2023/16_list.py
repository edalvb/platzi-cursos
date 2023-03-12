numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(type(numbers))

tasks = [
    'make a dishes',
    'clean the room',
    'wash the car',
    'buy a milk',
    'hola'
]

print(tasks)

types = [1, 2.0, '3', True, None]
print(types)
print(type(types))

print(numbers[0])
print(tasks[0])

# text = 'Hola'
# text[0] = 'h'

tasks[0] = 'make a coffee'
print(tasks)

tasks[0] = 'make a chocolate'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in tasks)
