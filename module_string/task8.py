# Бегущая строка

# Пользователь вводит две строки.
# Программа определяет, можно ли получить первую строку из второй циклическим сдвигом.
# Если это возможно, вычисляем величину сдвига:

first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')

result = False

# №1 Сдвиг влево:

if len(first_str) == len(second_str):
    for i_shift in range(1, len(first_str)):
        ver_str = ''
        for i_index in range(len(first_str)):
            index = (i_index + i_shift) % len(first_str)
            ver_str += second_str[index]
        if ver_str == first_str:
            result = True
            shift = i_shift
            break
if result:
    print(f'Первая строка получается из второй со сдвигом {shift}.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


# №2 Сдвиг вправо:

if len(first_str) == len(second_str):
    for i_shift in range(1, len(first_str)):
        second_str = second_str[-1] + second_str[:-1]
        if second_str == first_str:
            result = True
            shift = i_shift
            break
if result:
    print(f'Первая строка получается из второй со сдвигом {shift}.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')