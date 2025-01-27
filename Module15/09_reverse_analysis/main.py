n = int(input('Количество элементов в списке: '))
number_list = []


for i in range(n):
    number = int(input(f'Введите {i + 1} число в списке: '))
    number_list.append(number)
print(f'\nИзначальный список - {number_list}')

reverse_place = 1

print('Чётные числа в обратном порядке - ', end = '')
for index, num in enumerate(number_list):
    if number_list[index - reverse_place] % 2 == 0:
        print(number_list[index - reverse_place], end=' ')
    reverse_place += 2




