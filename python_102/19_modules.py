import sys
import re
import time
import collections as col

print(sys.path)

text = 'Mi número de telefono es 311 123 121, el código del pais es 57, mi número de la suerte es el 3'

print(re.findall('[0-9]+', text))

timestamp = time.time()
local = time.localtime(timestamp)
# resultado = time.strftime('%d/%m/%Y %H:%M:%S', local)
result = time.asctime(local)
print(result)

numbers = [1, 1, 2, 1, 3, 4, 5, 3, 2, 3, 4, 3, 4, 5, 2, 3, 4, 5, 1, 4]

counter = col.Counter(numbers)
print(counter)
