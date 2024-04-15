## Быстрая сортировка

# Реализуем алгоритм быстрой сортировки (ее называют сортировкой Хоара).

# За один шаг алгоритма выполняем следующие действия:

# 1. Выбираем один элемент списка (опорный элемент). В нашем случае опорным
# элементом всегда будет крайний правый.

# 2. Разбиваем текущий список на три части: элементы меньше опорного, равные
# опорному и больше опорного.

# 3. Для списков с элементами меньше и больше опорного, выполняем шаги 1 и 2.

# 4. Складываем результаты и получаем отсортированный список.

# Для удобства добавляем вспомогательную функцию, которая принимает на вход список,
# а возвращает три списка (с элементами меньше, равными и больше опорного).

def quicksort(lst):
    lst_1, lst_2, lst_3 = split(lst)
    if len(lst_1) > 1:
        lst_1 = quicksort(lst_1)
    if len(lst_3) > 1:
        lst_3 = quicksort(lst_3)
    return lst_1 + lst_2 + lst_3


def split(lst):
    result_1 = []
    result_2 = []
    result_3 = []
    support_elem = lst[-1]
    for elem in lst:
        if elem < support_elem:
            result_1.append(elem)
        elif elem == support_elem:
            result_2.append(elem)
        else:
            result_3.append(elem)
    return result_1, result_2, result_3


original_list = [4, 1, 5, 8, 11, 43, 4, 12, 7, 15, 9, 2, 7, 5]
sorted_list = quicksort(original_list)
print(sorted_list)
