# Симметричная последовательность

# Создаем список чисел

numbers = int(input('Количество чисел: '))
numbers_list = []

for _ in range(numbers):
    number = int(input('Число: '))
    numbers_list.append(number)

print('\nПоследовательность:', numbers_list)

# Проверяем последовательность чисел из списка на симметричность
# и определяем минимальное количество чисел, которое необходимо добавить
# в конец этой последовательности, чтобы она стала симметричной:

new_numbers_list = []

while True:
    reverse_numbers_list = numbers_list[::-1]
    if numbers_list == reverse_numbers_list:
        break
    else:
        new_numbers_list.insert(0, numbers_list[0])
        numbers_list.remove(numbers_list[0])

print('\nНужно приписать чисел:', len(new_numbers_list))
print('Сами числа:', new_numbers_list)

# Второй способ решения:

# count = 0
# while numbers_list != numbers_list[::-1]:
#     numbers_list.insert(numbers, numbers_list[count])
#     count += 1
#
# print('Нужно приписать чисел:', count)
# print('Сами числа:', numbers_list[:count][::-1])
