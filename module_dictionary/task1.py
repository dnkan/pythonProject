## Песни-2

# Песни хранятся в виде словаря. Программа запрашивает
# у пользователя количество песен из списка и их названия,
# а на экран выводит общее время их звучания:

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.38
}

num_songs = int(input('Сколько песен выбрать? '))

# sum_time = 0
time_list = []

for i_song in range(1, num_songs + 1):
    title_song = input(f'Название {i_song}-ой песни: ')
    # sum_time += violator_songs.get(title_song, 0)
    time_list.append(violator_songs.get(title_song, 0))

# sum_time = round(sum_time, 2)
sum_time = round(sum(time_list), 2)

print('Общее время звучания песен: {} минуты'.format(sum_time))
