# Файлы

# Программа получает на вход название файла и проверяет:
# -чтобы название не начиналось с одного из спец.символов: @,№,$,%,^,&,*,();
# -чтобы название заканчивалось расширением: .txt или .docx;

file_name = input('Название файла: ')

# Решение №1:

sym_str = '@,№,$,%,^,&,*,(,)'
exp_str = '.txt, .docx'

start = True
end = False

for i_sym in sym_str.split(','):
    if file_name.startswith(i_sym):
        start = False
        break

for i_exp in exp_str.split(', '):
    if file_name.endswith(i_exp):
        end = True
        break

if not start:
    print('Ошибка: название начинается недопустимым символом.')
if not end:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
if start and end:
    print('Файл назван верно.')

# Решение №2:

sym = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
exp = ('.txt', '.docx')

if file_name.startswith(sym):
    print('Ошибка: название начинается недопустимым символом.')
elif not file_name.endswith(exp):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')