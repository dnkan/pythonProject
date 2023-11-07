# Песни

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

sound_time = 0

# Запрашиваем у пользователя количество песен из списка, их название.
# Выводим общее время их звучания:

numbers_songs = int(input('Сколько песен выбрать? '))

for i_song in range(numbers_songs):
    print(f'Название {i_song + 1}-ой песни:', end=' ')
    user_song = input()
    for song in violator_songs:
        if user_song in song:
            sound_time += song[1]

print('Общее время звучания треков:', round(sound_time, 2), 'минуты')
