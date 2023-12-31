# Вечеринка

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# Запрашиваем у пользователя пришел или ушел гость.
# В зависимость от выбора, изменяем список гостей (гостей не может быть больше шести).
# Если пользователь вводит 'Пора спать', прерываем цикл:

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    choice = input('Гость пришел или ушел? ')
    if choice == 'Пора спать':
        print('Вечеринка закончилась. Все легли спать.')
        break
    name = input('Имя гостя: ')
    if choice == 'пришел':
        if len(guests) < 6:
            print(f'Привет, {name}!')
            guests.append(name)
        else:
            print(f'Прости, {name}, но мест нет.')
    if choice == 'ушел':
        print(f'Пока, {name}!')
        guests.remove(name)
