# Реализация генератора с помощью функции с ключевым словом yield
def fact(meaning):
    number = 1
    for i in range(meaning + 1):
        yield f'{number}! = {number}'
        number *= number + 1


for el in fact(5):
    print(el)
