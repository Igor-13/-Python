# Реализация функции суммы чисел


def my_func(number_1, number_2, number_3):
    return sum(sorted([int(number_1), int(number_2), int(number_3)])[1:])


print(my_func(number_1=input("Enter number 1: "), number_2=input("Enter number 2: "), number_3=input("Enter number 3: ")))