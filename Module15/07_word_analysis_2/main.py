word = input('Введите слово: ')
sym_list = list(word)
reverse_list = []
rev_index = 0

for _ in sym_list:
    rev_index -= 1
    reverse_list.append(sym_list[rev_index])

if reverse_list == sym_list:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
