import random

with open('./text.txt', 'w+') as f:
    for line in f:
        print(line)

    text = 'This is a new line ' + str(random.randint(1, 100)) + '\n';

    f.write(text)
    f.write('This is another new line\n')
    f.write('This is yet another new line\n')
