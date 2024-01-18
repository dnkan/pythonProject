import random

## "По парам".

# Программа инициализирует список из 10 случайных целых чисел,
# а затем делит эти числа на пары кортежей внутри списка:

first_lst = [random.randint(1, 9) for _ in range(10)]

second_lst_1 = [(value, first_lst[index + 1]) for index, value in enumerate(first_lst) if index % 2 == 0]
second_lst_2 = [(first_lst[i], first_lst[i + 1]) for i in range(0, 10, 2)]

print('Оригинальный список:', first_lst)
print('Новый список:', second_lst_1)
print(second_lst_2)
