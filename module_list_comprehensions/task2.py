# Генерация

length = int(input('Введите длину списка: '))

# Генерируем список в диапазоне (0, length - 1) с условиями: если число четное,
# то заменяем его на 1, нечетное - на остаток от деления на 5:

numbers_list = [(1 if numb % 2 == 0 else numb % 5) for numb in range(length)]

print('Результат:', numbers_list)