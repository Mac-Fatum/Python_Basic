n = int(input('Количество контейнеров: '))
container_list = []
count = 0

while count != n:
    for contain in range(n):
        weight = int(input(f'Введите массу контейнера: '))
        if 0 < weight <= 200:
            container_list.append(weight)
            count += 1
        else:
            print('Масса контейнера должна быть диапазоне от 1 до 200.')
print(container_list)

new_weight = int(input('\nВведите вес нового контейнера: '))
place = 0

for mass in container_list:
    if mass > new_weight:
        place += 1

print(f'\nНомер который получит новый контейнер - {place + 1}')



