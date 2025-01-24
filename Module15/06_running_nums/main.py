n = int(input('Количество элементов в списке? '))
shift = int(input('Сдвиг: '))
n_list = []
new_list = []

for i in range(n):
    item = int(input(f'Введите {i + 1} элемент списка: '))
    n_list.append(item)

new_place = 0
for index, item in enumerate(new_list):
    for i in range(index):
        i += 1
        if i > n:
            i = 0
    new_list.append()

print(new_list)
