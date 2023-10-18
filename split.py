def number_split(number):
    flag = True
    whole = ''
    fraction = ''
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole += symbol
        else:
            fraction += symbol
    return int(whole), int(fraction)

your_number = input('Введите число с точкой: ')

your_whole, your_fraction = number_split(your_number)

print(f'Целая часть числа: {your_whole}')
print(f'Число после точки: {your_fraction}')
