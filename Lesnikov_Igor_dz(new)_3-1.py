# Реализация функции деления числа


def division(number_1, number_2):
    try:
        result = int(number_1) / int(number_2)
    except ZeroDivisionError as err:
        return err
    except ValueError as err_2:
        return err_2
    else:
        return result


print(division(input("Enter number 1: "), input("Enter number 2: ")))