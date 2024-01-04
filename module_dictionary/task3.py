## Товары

# В первом словаре хранятся коды товаров, во втором - списки
# количества разнообразных товаров. Каждая запись второго словаря
# отображает, сколько и по какой цене (за штуку) закупалось товаров.

# Программа рассчитывает общую стоимость позиций для каждого товара:

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678'
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42}
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520}
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150}
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97}
    ]
}

for i_key, i_value in goods.items():
    total_count = 0
    total_cost = 0
    for i in range(len(store[i_value])):
        total_count += store[i_value][i]['quantity']
        total_cost += store[i_value][i]['quantity'] * store[i_value][i]['price']
    print('{} - {} штук, тоимость {} рубля.'.format(i_key, total_count, total_cost))