# Наименьший делитель

while 1:
    number = int(input('Введите число: '))
    if number > 1:
        search_number = number
        for i in range(number - 1, 1, -1):
            if number % i == 0:
                search_number = i
        print('Наименьший делитель отличный от единицы:', search_number)
    else:
        print('Ошибка ввода. Число должно быть больше единицы!')