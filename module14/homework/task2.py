
# Сумма и разность

def summa_numbers(n):
    summ = 0
    while n:
        summ += n % 10
        n //= 10
    return summ

def count_number(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count

N = int(input('Введите число: '))

res_summ = summa_numbers(N)
res_count = count_number(N)

print('Результат вычислений:', res_summ - res_count)
