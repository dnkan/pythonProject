## Продвинутая функция sum

# Программа реализует продвинутую функцию sum,
# которая умеет складывать числа из списка списков,
# из набора параметров:

def summ(*args):
    result = 0
    for arg in args:
        if isinstance(arg, list):
            result += summ(*arg)
        if isinstance(arg, int):
            result += arg
    return result


res = summ([1, 2, [3, 3, 4], 4, [1, 'b', 2, [1, 2, 3], 3], 11, [1, [13, 23], 5]])
print(res)
