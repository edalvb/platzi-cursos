items = [
    {
        'product': 'camisa',
        'price': 50
    },
    {
        'product': 'pantalon',
        'price': 100,
    },
    {
        'product': 'zapatos',
        'price': 150,
    }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)


def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item


items_v2 = list(map(add_taxes, items))
print(items)
print(items_v2)
