# Бегущие цифры

numbers_list = [1, -3, 4, 12, -2, 0, 27]

shift = int(input('Сдвиг: '))

# Корректируем величину сдвига, если она больше длины списка
shift %= len(numbers_list)

new_numbers_list = []

print('Изначальный список:', numbers_list)

# Циклически сдвигаем элементы списка вправо на величину сдвига
for index in range(len(numbers_list)):
    new_numbers_list.append(numbers_list[index - shift])

print('\nСдвинутый список:', new_numbers_list)
