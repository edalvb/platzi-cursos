def find_volume(length=1, width=1, depth=1):
    return length * width * depth, depth, 'hello'


result = find_volume(width=10)
print(result[1])

res, depth, text = find_volume(width=30)
print(res)
print(depth)
print(text)
