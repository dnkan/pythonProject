## Challenge-2

# Функция выводит все числа от 1 до num без использования циклов:

def print_number(num):
    if num == 0:
        return True
    print_number(num - 1)
    print(num)


user_number = int(input('Введите num: '))
print_number(user_number)
