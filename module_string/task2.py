# Самое длинное слово

# Вводится строка, содержащая пробелы и заканчивающаяся точкой.
# Находим самое длинное слово, выводим его и его длину.
# Если таких слов несколько, то выводим первое:

# Пример: я есть строка.

user_str = input('Введите строку: ').split()

user_str[-1] = user_str[-1][:-1]
max_word = 0
word = ''

for i_word in user_str:
    if len(i_word) > max_word:
        max_word = len(i_word)
        word = i_word

print('Самое длинное слово: "{}".'.format(word))
print('Длина этого слова: {} символов.'.format(max_word))
