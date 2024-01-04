## Криптовалюта

# Имеются данные в виде словаря. Необходимо обработать эти данные.

data = {
    'address': '0x544444444444',
    'ETH': {
        'balance': 444,
        'totalIn': 444,
        'totalOut': 4
    },
    'count_txs': 2,
    'tokens': [
        {
            'fst_token_info': {
                'address': '0x44444',
                'name': 'fdf',
                'decimals': 0,
                'symbol': 'dsfdsf',
                'total_supply': '3228562189',
                'owner': '0x44444',
                'last_updated': '1519022607901',
                'issuances_count': 0,
                'holders_count': 137528,
                'price': False
            },
            'balance': 5000,
            'totalIn': 0,
            'total_out': 0
        },
        {
            'sec_token_info': {
                'address': '0x44444',
                'name': 'ggg',
                'decimals': '2',
                'symbol': 'fff',
                'total_supply': '250000000000',
                'owner': '0x44444',
                'last_updated': '1520452201',
                'issuances_count': 0,
                'holders_count': 20707,
                'price': False
            },
            'balance': 5000,
            'totalIn': 0,
            'total_out': 0
        }
    ]
}

# Необходимо выполнить следующий алгоритм действий:

# 1. Вывести списки ключей и значений словаря:

print('Список ключей словаря "data":', data.keys())
print('Список значений словаря "data":', data.values())

# 2. В 'ETH' добавить ключ 'total_diff' со значением 100:

data['ETH']['total_diff'] = 100

print('\nСписок ключей словаря "ETH":', data['ETH'].keys())
print('Список значений словаря "ETH":', data['ETH'].values())

# 3. Внутри 'fst_token_info' значение ключа 'name' поменять с 'fdf' на 'doge':

data['tokens'][0]['fst_token_info']['name'] = 'doge'

print('\nСписок ключей словаря "fst_token_info":', data['tokens'][0]['fst_token_info'].keys())
print('Список значений словаря "fst_token_info":', data['tokens'][0]['fst_token_info'].values())

# 4. Удалить 'total_out' из 'tokens' и присвоеть его значение 'total_out' внутри 'ETH':

data['ETH']['totalOut'] = data['tokens'][0].pop('total_out')

print('\nСписок ключей словаря "ETH":', data['ETH'].keys())
print('Список значений словаря "ETH":', data['ETH'].values())

print('\nСписок ключей словаря "tokens[0]":', data['tokens'][0].keys())
print('Список значений словаря "tokens[0]":', data['tokens'][0].values())

# 5. Внутри 'sec_token_info' изменить название ключа 'price' на 'total_price':

data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

print('\nСписок ключей словаря "sec_token_info":', data['tokens'][1]['sec_token_info'].keys())
print('Список значений словаря "sec_token_info":', data['tokens'][1]['sec_token_info'].values())