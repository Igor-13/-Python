# Вывод каждого слова с новой строки
data = input(f'Введите несколько слов: ')
data = data.split(' ')

for num, word in enumerate(data, 1):
    if len(word) >= 10:
        print(f' {num}. - {word[:10]}')
    else:
        print(f' {num}. - {word}')

