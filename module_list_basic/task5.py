# Контейнеры

quantity = int(input('Количество контейнеров: '))
weights_list = []
print()

# Заполняем список величинами веса контейнеров (вес контейнера не более 200),
# список заполняется в порядке убывания веса
for i in range(quantity):
    weight = int(input('Введите вес контейнера: '))
    while weight > 200:
        print('Вес контейнера не должен превышать 200.')
        weight = int(input('Введите вес контейнера: '))
    if i > 0:
        while weight > weights_list[i-1]:
            print('Последовательность веса контейнера должна быть убывающей.')
            weight = int(input('Введите вес контейнера: '))
    weights_list.append(weight)

new_weight = int(input('\nВведите вес нового контейнера: '))

# Устанавливаем номер, под которым будет лежать новый контейнер
for index, weight in enumerate(weights_list):
    if new_weight > weight:
        print('\nНомер который получит новый контейнер:', index + 1)
        break

