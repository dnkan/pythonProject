# Годы

while True:
    first_year = int(input('Введите первый год (четырехзначное число): '))
    second_year = int(input('Введите второй год (четырехзначное число): '))
    if second_year > first_year:
        break
    else:
        print('Первый год не может быть больше второго. Попробуйте еще раз!')

print(f'Годы от {first_year} до {second_year} с тремя одинаковыми цифрами:')

for year in range(first_year, second_year + 1):
    string = str(year)
    substring = str(year % 10)
    count = string.count(substring)
    if count == 3:
        print(year)
    else:
        substring = str(year // 1000)
        count = string.count(substring)
        if count == 3:
            print(year)

