# Заглавные буквы

# Меняем регистр символов строки так, чтобы первая
# буква каждого слова была прописной, а остальные строчные:

user_str = input('Введите строку: ')

print('Результат:', user_str.title())

# Решение без использования метода title:

new_srt = []

for i_word in user_str.split():
    new_word = ''
    count = 0
    for i_let in i_word:
        if count == 0:
            new_word += i_let.upper()
        else:
            new_word += i_let.lower()
        count += 1
    new_srt.append(new_word)

print('Результат:', ' '.join(new_srt))
