# Ролики

# Пользователь вводит два списка: размер роликов и размер ног.
# Код определяет наибольшее количество людей, которые могут одновременно кататься.
# Человек может надеть ролики любого размера, которые не меньше размера его ноги:

numbers_rolls = int(input('Количество коньков: '))
numbers_people = int(input('Количество человек: '))

rolls_list = []
people_list = []
count = 0

for i_roll in range(numbers_rolls):
    print('Размер пары', i_roll + 1, end='')
    roll = int(input(': '))
    rolls_list.append(roll)

for i_people in range(numbers_people):
    print('Размер ноги человека', i_people + 1, end='')
    people = int(input(': '))
    people_list.append(people)

rolls_list.sort()
people_list.sort()

for people in people_list:
    for roll in rolls_list:
        if people <= roll:
            count += 1
            rolls_list.remove(roll)
            break


print('Наибольшее количество людей, которые могут взять ролики:', count)
