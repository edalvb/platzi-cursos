def increment(x):
    return x + 1


increment_v2 = lambda x: x + 1

print(increment(5))
print(increment_v2(5))

full_name = lambda name, last_name: f'{name} {last_name}'

print(full_name('Juan', 'Perez'))
