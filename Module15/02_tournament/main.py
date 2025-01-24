# TODO здесь писать код
tournament_participants = [
    "Артемий",
    "Борис",
    "Влад",
    "Гоша",
    "Дима",
    "Евгений",
    "Женя",
    "Захар",
    "Игорь",
    "Константин",
    "Максим",
    "Никита",
    "Павел",
    "Роман"
]
first_group = []
second_group = []

for index, name in enumerate(tournament_participants):
    if (index + 1) % 2 == 1:
        first_group.append(name)
    elif (index + 1) % 2 == 0:
        second_group.append(name)

print('Первая группа - ', end = '')
for a in first_group:
    print(f'{a}', end = ' ')

print('\nВторая группа - ', end = ' ')
for b in second_group:
    print(f'{b}', end = ' ')

