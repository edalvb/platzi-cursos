my_dict = {}
print(my_dict)
print(type(my_dict))

my_dict = {
    'name': 'John',
    'age': 30,
    'is_married': True,
    'lastname': 'Doe'
}

print(my_dict)
print(len(my_dict))

# Esta forma devuelve un error
print(my_dict['name'])
print(my_dict['age'])
# Esta forma devuelve None
print(my_dict.get('non'))

print('name' in my_dict)
print('non' in my_dict)
