## Три списка.

# Даны три списка. Нужно выполнить две задачи:

# 1. найти элементы, которые есть в каждом списке;
# 2. найти элементы из первого списка, которых нет во втором и третем списке.

# Каждую задачу нужно выполнить двумя способами:

# 1. без использования множеств;
# 2. с использованием множеств.

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

new_array = []

for num in array_1:
    if num in array_2 and num in array_3:
        new_array.append(num)

print('Вывод:\nЗадача 1:\nРешение без множеств:', *new_array)

array_set_1 = set(array_1)
array_set_2 = set(array_2)
array_set_3 = set(array_3)

new_array_set = array_set_1.intersection(array_set_2)
new_array_set = new_array_set.intersection(array_set_3)

print('Решение с множествами:', *sorted(new_array_set))

new_array = []

for num in array_1:
    if num not in array_2 and num not in array_3:
        new_array.append(num)

print('\nЗадача 2:\nРешение без множеств:', *new_array)

new_array_set = array_set_1.difference(array_set_2)
new_array_set = new_array_set.difference(array_set_3)

print('Решение с множествами:', *sorted(new_array_set))

