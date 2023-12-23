# Пароль

# Просим пользователя придумать пароль до тех пор,
# пока он не будет соответствовать требованиям надежности.
# Пароль должен состоять минимум из восьми символов,
# содержать хотя бы одну заглавную букву и не менее трех цифр:

while True:
    user_password = input('Придумайте пароль: ')
    if len(user_password) > 7:
        count_upper = 0
        count_int = 0
        for i_sym in user_password:
            if i_sym.isupper():
                count_upper += 1
            if i_sym.isdigit():
                count_int += 1
        if count_upper > 0 and count_int > 2:
            break
    print('Пароль ненадежный. Попробуйте еще раз.')

print('Это надежный пароль.')

