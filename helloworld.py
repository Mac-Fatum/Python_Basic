films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

my_films = []

while True:
    print(f'\nВаш текущий топ фильмов: {my_films}')
    film = input('Название фильма: ')
    if film in films:
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            if film not in my_films:
                my_films.append(film)
            else:
                print('Фильм уже в вашем каталоге.')
        if command == 'вставить':
            index = int(input('На какое место? '))
            my_films.insert(index - 1, film)
        if command == 'удалить':
            my_films.remove(film)
    else:
        print('Данного фильма на нашем сайте')
