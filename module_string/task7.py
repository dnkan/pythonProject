# IP-адрес 2

# Пользователь вводит строку. Программа определяет,
# действительно данная строка - правильный IP-адрес. Обеспечен контроль ввода,
# где предусматривается добавление целых чисел от 0 до 255 и точек между ними:

user_ip = input('Введите IP: ').split('.')

if len(user_ip) != 4:
    print('Адрес - это четыре числа, разделенные точками.')
else:
    for i_elem in user_ip:
        if not i_elem.isdigit():
            print(f'{i_elem} - это не целое число.')
            break
        if int(i_elem) > 255:
            print(f'{i_elem} превышает 255.')
            break

    else:
        print('IP-адрес корректен.')