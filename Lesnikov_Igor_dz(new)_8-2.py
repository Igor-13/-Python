# Реализация класса-исключения

class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Division:

    def __floordiv__(self, other, other_2):
        self.other = other
        self.other_2 = other_2

    def div(self, other, other_2):
        try:
            if other_2 == 0:
                raise Error("На ноль делить нельзя!")
        except Error as err:
            print(err)
        else:
            result = other // other_2
            print(result)


x = Division()
x.div(5, 0)
