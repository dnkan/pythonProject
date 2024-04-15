## Список списков - 2

# Данн список с неограниченным количеством вложенных списков и разным уровнем вложенности.
# Рекурсивная функция, которая раскрывает все вложенные списки,
# т.е. оставляет только внешний список:

def flatten(lst):
    new_list = []
    for elem in lst:
        if isinstance(elem, int):
            new_list.append(elem)
        else:
            new_list += flatten(elem)
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

nice_list = flatten(nice_list)
print('Ответ:', nice_list)
