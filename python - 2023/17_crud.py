# CRUD

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

numbers[1] = 20
print(numbers[1])

numbers.append(800)
print(numbers)

numbers.insert(0, 'hello')
print(numbers)

numbers.insert(3, 'world')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = tasks + numbers
# print(new_list)

numbers[2] = 'hello!!!'

# print(numbers)
# print(new_list)

index = new_list.index('hello')
new_list[index] = 'todo change'
print(new_list, '\n')

new_list.remove('todo change')
print(new_list, '\n')

new_list.pop()
print(new_list, '\n')

new_list.pop(0)
print(new_list, '\n')

new_list.reverse()
print(new_list, '\n')

numbers_a = [1, 4, 3, 2, 5]
numbers_a.sort()
print(numbers_a, '\n')

strings = ['a', 'd', 'c', 'b']
strings.sort()
print(strings, '\n')

new_list.sort()
# this will not work
# print(new_list, '\n')
