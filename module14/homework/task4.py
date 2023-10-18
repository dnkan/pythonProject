# Монетка-2

import math

def calculation(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    check(r, c)

def check(a1, b1):
    if a1 >= b1:
        print('Монетка где-то рядом.')
    else:
        print('Монетки в области нет.')

print('Введите координаты монетки:')

x = float(input('X: '))
y = float(input('Y: '))

r = float(input('Введите радиус: '))

calculation(x, y)

