n = int(input('Количество элементов в списке: '))
number_list = []


for i in range(n):
    number = int(input(f'Введите {i + 1} число в списке: '))
    number_list.append(number)
print(f'\nИзначальный список - {number_list}')

for num in range(len(number_list) - 1, -1):
    if number_list[num] % 2 == 0:
        print(num, end = ' ')

