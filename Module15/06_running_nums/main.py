n = int(input('Количество элементов в списке? '))
shift = int(input('Сдвиг: '))
n_list = []
new_list = []

for i in range(n):
    item = int(input(f'Введите {i + 1} элемент списка: '))
    n_list.append(item)

for index, num in enumerate(n_list):
    index += 1
print(n_list)
print(new_list)






