## Словарь синонимов

# На вход в программу подается N пар слов.
# Каждое слово является синонимом для своего парного слова.

# Пример: Привет - Здравствуйте.

# Код составляет словарь синонимов, затем запрашивает у
# пользователя слово и выводит на экран его синоним.
# Проверка не должна зависить от регистра символов:

number_pairs = int(input('Введите количество пар слов: '))

pairs_dict = dict()

for i_pair in range(1, number_pairs + 1):
    words = input(f'{i_pair}-ая пара: ').split()
    pairs_dict[words[0]] = words[2]

while True:
    user_word = input('Введите слово: ').capitalize()
    if pairs_dict.get(user_word):
        print('Синоним:', pairs_dict[user_word])
        break
    print('Такого слова в словаре нет.')

