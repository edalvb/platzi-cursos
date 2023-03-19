import functools as ft

numbers = [1, 2, 3, 4]


def accum(counter, item):
    print(counter, item)
    return counter + item


result = ft.reduce(accum, numbers, 6)

print(result)
