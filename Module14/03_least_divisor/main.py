# TODO здесь писать код
def divider(num):
    small_d = 0
    for div in range(2, num + 1):
        if num % div == 0:
            small_d = div
            break
    return small_d

number = int(input('Введите число: '))
print(f'Наименьший делитель, отличный от единицы: {divider(number)}')


