x = 10

try:
    print(0 / 0)
    assert 1 != 1, '1 is not equal to 1'
    if x < 18:
        raise Exception('x should be 18')
except ZeroDivisionError as err:
    print(err)
except AssertionError as err:
    print(err)
except Exception as err:
    print(err)

print('Done.')
