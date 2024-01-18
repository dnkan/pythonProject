## "Контакты - 3".

# Программа бесконечно запрашивает у пользователя действие,
# которое он хочет совершить: добавить контакт или найти человека
# в списке контактов по фамилии:

phone_dict = dict()

while True:
    user_choice = int(input('\nВыберите действие:'
                            '\n1 - добавить контакт;'
                            '\n2 - найти человека по фамилии: '))
    if user_choice == 1:
        name = input('\nИмя, Фамилия контакта (через пробел): ')
        name = tuple(name.split())
        if name in phone_dict:
            print('Контакт уже существует.')
        else:
            phone_number = int(input('Номер телефона: '))
            phone_dict[name] = phone_number
            print('\nТекущий список контактов:')
            for name, num in phone_dict.items():
                print(*name, ':', num)

    if user_choice == 2:
        surname = input('\nФамилия контакта: ').lower()
        for name, num in phone_dict.items():
            if surname in name[1].lower():
                print(*name, ':', num)
