## Глубокое копирование

# Программа запрашивает у пользователя количество сайтов, затем названия продуктов,
# а после каждого запроса выводит на экран активные сайты.

import copy

site = {
        'html': {
            'head': {
                'title': 'Куплю/продам product недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на product',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }

site_list = []


def product_site(data, name):
    if 'title' in data:
        data['title'] = 'Куплю/продам {product} недорого'.format(product=name)
    if 'h2' in data:
        data['h2'] = 'У нас самая низкая цена на {product}'.format(product=name)
    for sub_data in data.values():
        if isinstance(sub_data, dict):
            product_site(sub_data, name)


count_sites = int(input('Укажите количество сайтов: '))

for _ in range(count_sites):
    name_product = input('Укажите название продукта: ')
    copy_site = copy.deepcopy(site)
    product_site(copy_site, name_product)
    site_list.append(copy_site)

print(*site_list, sep='\n')
