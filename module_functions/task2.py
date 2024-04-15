## Поиск элемента-2

# Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную
# глубину - уровень, до которого будет просматриваться структура.

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body':  {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь, новый абзац'
        }
    }
}


def search_key(data, key, deep_search):
    if key in data:
        return data[key]

    if deep_search:
        deep_search -= 1
        if deep_search == 0:
            return None

    for i_value in data.values():
        if isinstance(i_value, dict):
            result = search_key(i_value, key, deep_search)
            if result:
                break
    else:
        result = None

    return result


user_key = input('Введите искомый ключ: ')
choice = input('Хотите ввести максимальную глубину? Y/N ').upper()
if choice == 'Y':
    user_deep_search = int(input('Введите максимальную глубину: '))
else:
    user_deep_search = None

value = search_key(site, user_key, user_deep_search)
print('Значение ключа:', value)
