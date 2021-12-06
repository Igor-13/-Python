# Реализация функции вывода данных


def data(**kwargs):
    return ', '.join(kwargs.values())


print(data(name=input("Enter your name: "), surname=input("Enter your surname: "), year_of_birth=input("Enter your "
                                                                                                       "year of "
                                                                                                       "birth: "),
           city_of_residence=input("Enter your city of residence: "), email=input("Enter your email: "), phone=input(
        "Enter your phone: ")))
