price = 100  # global variable


def increment():
    # mofiying global variable
    # global price
    price = 0  # local variable
    result = price + 10
    print(result)
    return result


print(increment())
print(price)
