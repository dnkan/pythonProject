# Видеокарты

nums_card = int(input('Количество видеокарт: '))
card_list = []
new_card_list = []

# Заполняем список видеокарт цифрами, обозначающими модель и поколение видеокарты
for i in range(nums_card):
    print(f'Видеокарта {i + 1}:', end=' ')
    card = int(input())
    card_list.append(card)

# Устанавливаем самые старшие поколения видеокарт
max_card = max(card_list)

# Заполняем новый список без старших поколений видеокарт
for card in card_list:
    if card != max_card:
        new_card_list.append(card)

print('Старый список видеокарт:', card_list, '\nНовый список видеокарт:', new_card_list)