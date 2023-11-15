# Список списков

# Дан многомерный список: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
# [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]. Код раскрывает все списки,
# оставив только внешний список:

nice_list = [
    [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]
    ],
    [
        [10, 11, 12], [13, 14, 15], [16, 17, 18]
    ]
]

result_1 = [
    nice_list[i][j][k]
    for i in range(2)
    for j in range(3)
    for k in range(3)
]

# Или:

result_2 = [
    number
    for nested_list_1 in nice_list
    for nested_list_2 in nested_list_1
    for number in nested_list_2
]

print(result_1, '\n', result_2, sep='')

# Решение без использования LC:

# result = []
#
# for i in range(2):
#     for j in range(3):
#         for k in range(3):
#             result.append(nice_list[i][j][k])
#
# print(result)