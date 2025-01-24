# TODO здесь писать код
number = int(input('Количество видеокарт: '))
graphics_card = []
high = 0

for _ in range(number):
    device = int(input('Видеокарта: '))
    graphics_card.append(device)
    if device > high:
        high = device
print(f'Старый список видеокарт - {graphics_card}')

for dev in graphics_card:
    if dev == high:
        graphics_card.remove(dev)
print(f'Новый список видеокарт - {graphics_card}')



