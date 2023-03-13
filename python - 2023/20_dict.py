person = {
    'name': 'nico',
    'lastname': 'serrano',
    'langs': ['python', 'javascript', 'c#'],
    'age': 99,
}
print(person, '\n')

person['name'] = 'Nicolás'
print(person, '\n')

person['age'] -= 50
print(person, '\n')

person['langs'].append('java')
print(person, '\n')

del person['lastname']
print(person, '\n')

# también se puede usar pop para eliminar un elemento
person.pop('age')
print(person, '\n')

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())





