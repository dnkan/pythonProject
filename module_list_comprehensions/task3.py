import random

# Случайные соревнования

# Генерируем два списка длиной 20 из случайных вещественных чисел от 5 до 10.
# Затем генерируем третий список из наибольших чисел с равными индексами:

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners_list = [
    first_team[i] if first_team[i] > second_team[i]
    else second_team[i] for i in range(20)
]

print('Первая команда:', first_team)
print('\nВторая команда:', second_team)
print('\nПобедители тура:', winners_list)
