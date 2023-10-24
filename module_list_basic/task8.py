# Сортировка

numbers_list = [10, 8, 25, -1, 0, 8, 5, 0, -3]

print('Изначальный список:', numbers_list)

# Сортируем список чисел в порядке возрастания (от min к max)
for i in range(len(numbers_list)):
    for j in range(i, len(numbers_list)):
        if numbers_list[j] < numbers_list[i]:
            numbers_list[j], numbers_list[i] = numbers_list[i], numbers_list[j]

print('Отсортированный список:', numbers_list)
