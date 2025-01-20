# TODO здесь писать код
def summ(num):
    sum_n = 0
    while num != 0:
        sum_n += num % 10
        num //= 10
    return sum_n

def count(num):
    count_n = 0
    while num != 0:
        count_n += 1
        num //= 10
    return count_n

number = int(input('Введите число: '))
print(f'\nСумма чисел: {summ(number)}'
      f'\nКоличество цифр в числе: {count(number)}'
      f'\nРазность суммы и количества цифр: {summ(number) - count(number)} ')
