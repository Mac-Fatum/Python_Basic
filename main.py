goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print(f'Текущий ассортимент - {goods}')

new_fruit = input('\nНовый фрукт: ')
price = int(input('Цена: '))

goods.append([new_fruit, price])
print(f'\nНовый ассортимент - {goods}')

for i_list in goods:
    i_list[1] = round(i_list[1] * 1.08, 2)

print(f'\nНовый ассортимент с увеличенной ценой - {goods}')