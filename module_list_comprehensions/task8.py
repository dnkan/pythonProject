# Шифр Цезаря

alphabet = [
    'a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
    'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
    'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]

user_text = input('Введите сообщение: ')

user_shift = int(input('Введите сдвиг: '))

new_text = ''

# Для шифрования введенного текста, меняем каждую букву текста
# на следующую по алфавиту через shift позиций по кругу:

for symbol in user_text:
    if symbol in alphabet:
        new_index = (alphabet.index(symbol) + user_shift) % len(alphabet)
        new_text += alphabet[new_index]
    else:
        new_text += symbol

print('Зашифрованное сообщение:', new_text)

# Решение задачи с использованием LC:

def code_func(shift, text):
    new_text = ''
    symbol_list = [((alphabet[(alphabet.index(symbol) + shift) % len(alphabet)])
         if symbol in alphabet else symbol) for symbol in text]
    for symbol in symbol_list:
        new_text += symbol
    return new_text

alphabet = 'aбвгдеёжзийклмнопрстуфхцчшщъыьэюя'

new_text = code_func(user_shift, user_text)

print('Зашифрованное сообщение:', new_text)

