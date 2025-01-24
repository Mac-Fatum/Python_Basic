films_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
my_films = []
number = int(input('Сколько фильмов хотите добавить? '))

for i in range(number):
    film = input('Введите название фильма: ')
    if film in films_list:
        my_films.append(film)
    else:
        print(f'Ошибка - фильма {film} у нас нет :(')

print('\nВаш список любимых фильмов: ', end = '')
for i in my_films:
    print(f'{i}, ', end = '')