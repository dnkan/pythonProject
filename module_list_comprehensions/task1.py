# Гласные буквы

# Проверяем введеный пользователем текст на количество гласных букв.
# Выводим количество и список гласных букв из текста:

vowel_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

user_text = input('Введите текст: ')

new_list = [letter for letter in user_text if letter in vowel_letters]

print('Список гласных букв:', new_list)
print('Длина списка:', len(new_list))