'''
for el in range(20):
    print(el)
'''

my_list = [23, 45, 67, 89, 43]
for e in my_list:
    print(e)

my_tuple = ('nico', 'juli', 'luis', 'jose', 'maria')
for e in my_tuple:
    print(e)

print('\n')

my_dict = {'name': 'nico', 'age': 23, 'country': 'colombia'}
for e in my_dict:
    print(e, ' => ', my_dict[e])

for clave, valor in my_dict.items():
    print(clave, ' => ', valor)

people = [
    {'name': 'nico', 'age': 23, 'country': 'colombia'},
    {'name': 'juli', 'age': 24, 'country': 'colombia'},
    {'name': 'luis', 'age': 25, 'country': 'colombia'},
    {'name': 'jose', 'age': 26, 'country': 'colombia'},
    {'name': 'maria', 'age': 27, 'country': 'colombia'}
]

for person in people:
    print(person['name'], ' => ', person['age'])
