# Реализация 2-х скриптов
from itertools import count, cycle

meaning_1 = count(10)
meaning_2 = cycle('qwerty')

for n in range(6):
    print(next(meaning_1), next(meaning_2))
