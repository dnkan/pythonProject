# Кино

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']

favourite_films = []

quantity = int(input('Сколько фильмов хотите добавить? '))

# Заполняем список любимых фильмов, если указаный вами фильм не в списке film,
# то появится сообщение об ошибке, и фильм не добавится в список любимых
for i in range(quantity):
    film = input('Введите название фильма: ')
    if film not in films:
        print(f'Ошибка. Фильма {film} у нас нет.')
    else:
        favourite_films.append(film)

print('\nВаш список любимых фильмов:', favourite_films)