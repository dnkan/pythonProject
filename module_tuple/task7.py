## "Своя функция zip".

# Даны строка и кортеж из чисел. Программа создает генератор
# из пар кортежей "символ - число":

u_str = 'abcd'
u_tpl = 10, 20, 30, 40

# u_str = {'as': 1, 'bs': 2, 'cs': 3, 'ds': 4}
# u_tpl = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Проверка типа данных на словарь
if isinstance(u_str, dict):
    u_str = u_str.values()

if isinstance(u_tpl, dict):
    u_tpl = u_tpl.values()

u_zip = ((sym, num) for i_index, sym in enumerate(u_str)
         for j_index, num in enumerate(u_tpl) if i_index == j_index)

print(u_zip)

for elem in u_zip:
    print(elem)
