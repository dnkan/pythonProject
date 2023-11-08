# Ролики

# Пользователь вводит два списка: размер роликов и размер ног.
# Код определяет наибольшее количество людей, которые могут одновременно кататься.
# Человек может надеть ролики любого размера, которые не меньше размера его ноги:

numbers_rolls = int(input('Количество коньков: '))
numbers_people = int(input('Количество человек: '))

rolls_list = []
foot_list = []
count = 0

for i_roll in range(numbers_rolls):
    print('Размер пары', i_roll + 1, end='')
    roll = int(input(': '))
    rolls_list.append(roll)

for i_foot in range(numbers_people):
    print('Размер ноги человека', i_foot + 1, end='')
    foot = int(input(': '))
    foot_list.append(foot)

rolls_list.sort()
foot_list.sort()

for foot in foot_list:
    for roll in rolls_list:
        if foot <= roll:
            count += 1
            rolls_list.remove(roll)
            break


print('Наибольшее количество людей, которые могут взять ролики:', count)
