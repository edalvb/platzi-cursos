file = open('./text.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# file.close()

with open('./text.txt') as f:
    for line in f:
        print(line)
