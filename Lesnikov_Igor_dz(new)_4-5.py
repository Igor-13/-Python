# Определение элемента списка, не имеющего повторений
from functools import reduce


def numbers(meaning_1, meaning_2):
    return meaning_1 * meaning_2


result = [n for n in range(100, 1001, 2)]

print(reduce(numbers, result))
