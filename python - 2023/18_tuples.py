numbers = (1, 2, 3, 5)
strings = ("one", "two", "three", "five")
print(numbers)
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])
print(type(strings))

print(strings)
print(type(strings))

# CRUD
# Create
# numbers.append(6)
print(numbers)
# numbers[1] = 'change'

print(strings.index('five'))
print(strings.index('one'))

my_list = list(strings)
print(my_list)
print(type(my_list), '\n')

my_list[1] = 'change'
print(my_list, '\n')

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
