# Турнир

names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list = []

# Заполняем новый список каждым вторым именем из первого списка
for index in range(len(names_list)):
    if index % 2 == 0:
        new_list.append(names_list[index])

# Иной способ
# for index, name in enumerate(names_list):
#     if index % 2 == 0:
#         new_list.append(name)

print('Первый день:', new_list)
