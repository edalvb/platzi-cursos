def increment(x):
    return x + 1


increment_v2 = lambda x: x + 1


def higher_order_function(f, x):
    return x + f(x)


hof = lambda f, x: x + f(x)

print(higher_order_function(increment, 2))

print(hof(increment_v2, 2))
print(hof(lambda x: x + 3, 2))
print(hof(lambda x: x * 2, 2))
