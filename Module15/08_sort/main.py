n = int(input('Количество элементов в списке: '))
n_list = []

for i in range(n):
    item = int(input(f'Введите {i + 1} число в списке: '))
    n_list.append(item)
print(f'\nИзначальный список - {n_list}')

for i in range(n - 1):
    for index in range(n - 1 - i):
        if n_list[index] > n_list[index + 1]:
            n_list[index], n_list[index + 1] = n_list[index + 1], n_list[index]
print(f'\nОтсортированный список - {n_list}')
