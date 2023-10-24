# Генерация списка

N = int(input('Введите число: '))

nums_list = []

# Заполняем список нечетными числами
for num in range(1, N + 1):
    if num % 2 != 0:
        nums_list.append(num)

print(f'Список из нечетных чисел от 1 до {N}:', nums_list)
