## Снова палиндром

# Пользователь вводит строку. Программа определяет, существует ли
# у этой строки перестановка, при которой она станет палиндромом:

user_string = input('Введите строку: ')

symbol_dict = dict()

for sym in user_string:
    if sym in symbol_dict:
        symbol_dict[sym] += 1
    else:
        symbol_dict[sym] = 1

count = 0

for num in symbol_dict.values():
    if num % 2 != 0:
        count += 1

if count > 1:
    print('Нельзя сделать полиндром.')
else:
    print('Можно сделать полиндром.')
