# Анализ слова - 2

word = input('Введите слово: ')

word_list = list(word)

new_word = ''

# Изменяем строку в строку наоборот (иной способ со стороками)
# for sym in word[::-1]:
#     new_word += sym

# Меняем противоположные элементы списка местами (первый-последний, второй-предпоследний и т.д.)
for index in range(len(word) // 2):
    word_list[index], word_list[len(word) - index - 1] \
        = word_list[len(word) - index - 1], word_list[index]

# Преобразуем полученный список в строку
for letter in word_list:
    new_word += letter

if word == new_word:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')
