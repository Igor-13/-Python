# Реализация функции числа в степень


def my_func(x, y):

    x = float(x)
    y = int(y)
    answer = 1
    for z in range(abs(y)):
        answer /= x

    return f' Число x в степени y равно: {answer}'


print(my_func(2, -3))
