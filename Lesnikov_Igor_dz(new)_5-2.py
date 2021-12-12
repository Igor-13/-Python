# Подсчёт количества строк и слов в каждой строке файла.


with open('text_3.txt', 'r', encoding='utf-8') as z:
    line = z.readlines()
    for x, y in enumerate(line, 1):
        word = len(y.split())
        print(f'Строк: {x} - {word} слов')

