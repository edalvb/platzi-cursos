text = 'Ella sabe Python'
print(text[0])
print(text[1])
# print(text[999])
size = len(text)
print(text[size - 1])
print(text[-1])

# slicing
print(text[0:4])
print(text[5:9])
print(text[10:16])
print(text[:4])
print(text[5:])
print(text[:])

# slicing with step
print(text[0:16:2])
print(text[::2])

# reverse
print(text[::-1])
