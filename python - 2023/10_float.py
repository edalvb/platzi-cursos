x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x == y)

# Resolver con strings
print(str(x) == str(y))

y_str = format(y, '.2g')
print(y_str) # 3.3
print(str(x) == y_str)

print("*" * 10)
# Resolver con tolerancia
tolerancia = 0.00001
print(abs(x - y) < tolerancia)

print(x == round(y, 1))
