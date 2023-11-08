# Считалка

# Ползователь задает количество человек и номер убывающего человека:

number_peoples = int(input('Количество человек в считалке: '))
number_delete = int(input('Какое число в считалке? '))

print(f'\nЗначит выбывает каждый {number_delete}-ой человек.')

# Создаем список игроков от 1 до номера, заданного пользователем,
# задаем начало считалки с первого номера в списке и проходимся по списку на один раз меньше,
# чем количество игроков, за один проход по циклу удаляем одного игрока, при этом контролируем,
# чтобы номер убывающего игока не превышал количества оставшихся игроков:

people_list = list(range(1, number_peoples + 1))
index = 0

for _ in range(number_peoples - 1):
    print('\nТекущий круг людей:', people_list)
    print('Начало счета с номера:', people_list[index])
    index = (index + number_delete - 1) % len(people_list)
    print('Выбывает человек под номером:', people_list[index])
    people_list.remove(people_list[index])
    index %= len(people_list)

print('\nОстался человек под номером', *people_list)
