n = int(input('Количество элементов в списке? '))
shift = int(input('Сдвиг: '))
n_list = []
new_list = []

for i in range(n):
    item = int(input(f'Введите {i + 1} элемент списка: '))
    n_list.append(item)


new_place = 0
for index in range(n):
    new_place += shift
    if new_place > n:
        new_place = 0
for i in range(n):
    n_list[i] = n_list[new_place]

print(n_list)
print(new_list)

