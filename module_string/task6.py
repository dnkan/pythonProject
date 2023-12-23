# Сжатие

# Специальное кодирование: s = 'aaabbccccbba' преобразуется в 'a3b2c4b2a1'.
# Программа считывает строку, кодирует ее и выводит на экран результат.
# Код учитывает регистр символов:

user_str = input('Введите строку: ')

result = []
prev_sym = user_str[0]
count = 0

for i_sym in user_str:
    if i_sym == prev_sym:
        count += 1
    else:
        result.append(prev_sym)
        result.append(str(count))
        count = 1
        prev_sym = i_sym

result.append(prev_sym)
result.append(str(count))

print('Закодированная строка:', ''.join(result))
