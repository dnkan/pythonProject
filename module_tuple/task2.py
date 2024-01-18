## "Универсальная программа".

# Функция возвращает список элементов итерируемого объекта
# (кортежа, строки, списка, словаря), у которого индекс -
# это простое число.
# Функция is_prime - для проверки на простое число.

def is_prime(num):
    if num > 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True


def crypto(sequence):
    if isinstance(sequence, dict):
        sequence = sequence.values()
    return [value for ind, value in enumerate(sequence) if is_prime(ind)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(crypto('О Дивный Новый мир!'))

print(crypto((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

print(crypto({0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'k'}))
