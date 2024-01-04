## Пицца

# На вход в программу подается N заказов. Каждый заказ представляет
# собой строку вида "Покупатель - название пиццы - количество заказанных пицц".

# Пример: Иванов Пепперони 2

# Программа выводит список покупателей и их заказов по алфавиту. Один человек
# может заказать одну и ту же пиццу несколько раз:

number_orders = int(input('Введите количество заказов: '))

orders_dict = dict()

for i_order in range(1, number_orders + 1):
    order = input(f'{i_order}-ый заказ: ').split()
    if order[0] not in orders_dict:
        orders_dict[order[0]] = {order[1]: int(order[2])}
    else:
        if order[1] in orders_dict[order[0]]:
            orders_dict[order[0]][order[1]] += int(order[2])
        else:
            orders_dict[order[0]][order[1]] = int(order[2])

for key in orders_dict:
    print(f'{key}:')
    for i_key in orders_dict[key]:
        print(f'{i_key}: {orders_dict[key][i_key]}')
