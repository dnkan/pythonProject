# Шеренга

# Функция добавления чисел из первого списка во второй по возрастанию:
def sorted_func(list_1, list_2):
    for num_1 in list_1:
        for index, num_2 in enumerate(list_2):
            if num_1 < num_2:
                list_2.insert(index, num_1)
                break

# Функция сортирования списка чисел по возрастанию:
def sorted_func(list):
    for i_num in range(len(list)):
        for j_num in range(i_num, len(list)):
            if list[j_num] < list[i_num]:
                list[i_num], list[j_num] = list[j_num], list[i_num]

# Генерируем список от 160 до 176 с шагом 2:

first_rank = list(range(160, 177, 2))

# Генерируем список от 162 до 180 с шагом 3:

second_rank = list(range(162, 181, 3))

# Объединяем оба списка в один и сортируем по возрастанию (3 решения):

# № 1:
# sorted_func(first_rank, second_rank)
# print('Отсортированный список:', second_rank)

# № 2:
# first_rank.extend(second_rank)
# first_rank.sort()
# print('Отсортированный список:', first_rank)

# № 3:
second_rank.extend(first_rank)
sorted_func(second_rank)
print('Отсортированный список:', second_rank)



