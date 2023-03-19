# print(0 / 0)
# print(result)
print('Done.')

suma = lambda x, y: x + y
assert suma(2, 2) == 4

print('Done.')

x = 10
if x < 18:
    raise Exception('x should be 18')
