text = 'Ella sabe programar en Python'
# Busca si la palabra 'programar' está en la variable text
# In verifica si la palabra está en la variable
'''
print('programar' in text)

if 'Python' in text:
    print('Python está en la variable text')
else:
    print('Python no está en la variable text')

size = len(text)
print(size)
'''

# Métodos de cadenas
print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))

print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Go'))

text2 = 'este es un titulo'

print(text2)
print(text2.capitalize())
print(text2.title())
print(text2.isdigit())
print('123'.isdigit())
