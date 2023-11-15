# Двумерный список

# Генерируем думерный список: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

result = [[j for j in range(i, 13, 4)] for i in range(1, 5)]

# Генерация двумерного списка не используя LC:

# result = []
# inter = []
# for i in range(1, 5):
#     for j in range(i, 13, 4):
#         inter.append(j)
#     result.append(inter)
#     inter = []

print(result)
