def sum_with_range(min, max):
    sum = 0

    for x in range(min, max):
        sum += x

    return sum


print(sum_with_range(1, 10))
print(sum_with_range(10, 30))
print(sum_with_range(1, 100))
