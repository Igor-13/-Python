# Запись в файл программно набор чисел, разделённых пробелами
from random import randint

with open('text_13.txt', 'w+', encoding='utf-8') as z:
    z.write(' '.join([str(randint(1, 1000)) for _ in range(100000)]))
    z.seek(0)
    print(sum(map(int, z.readlines().split())))
