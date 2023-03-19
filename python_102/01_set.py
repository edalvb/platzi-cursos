set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 2.3, 'col', True}
print(set_types)

set_from_string = set('hello')
print(set_from_string)

set_from_tuple = set(('col', 'mex', 'bol'))
print(set_from_tuple)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_from_list = set(numbers)
print(set_from_list)

unique_numbers = list(set_from_list)
print(unique_numbers)
