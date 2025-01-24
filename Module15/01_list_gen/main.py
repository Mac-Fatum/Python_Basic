# TODO здесь писать код
n = int(input('Введите число: '))
num_list = []

for num in range(1, n + 1, 2):
    num_list.append(num)

print(f'Список нечетных чисел от 1 до N - {num_list}')