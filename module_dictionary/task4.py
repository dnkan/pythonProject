## Гистограмма частоты-2

# Программа получает на вход текст и считает сколько
# раз каждый символ встречается в тексте. Написанная функция
# инвентирует словарь, т.е. в качестве ключа будет частота,
# а в качестве значения - список символов с этой частотой:

def invert(user_dict):
    new_dict = dict()
    for key, value in user_dict.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)

    return new_dict

text = input('Введите текст: ')

sym_dict = dict()

for sym in text:
    if sym not in sym_dict:
        sym_dict[sym] = 1
    else:
        sym_dict[sym] += 1

print('Оригинальный словарь частот:')

for key in sorted(sym_dict):
    print(key, ':', sym_dict[key])

inv_dict = invert(sym_dict)

print('\nИнвертированный словарь частот:')

for key in sorted(inv_dict):
    print(key, ':', inv_dict[key])