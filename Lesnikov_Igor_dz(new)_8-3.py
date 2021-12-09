# Реализация класса-исключения на проверку чисел
class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Number:

    def __init__(self, meaning):
        self.meaning = meaning

    def examination(self, meaning):
        result = []
        while meaning != 'stop':
            try:
                meaning = input('Введите значение')
                if not meaning.isdigit():
                    raise Error("Введите другое значение")
            except Error as err:
                print(err)
            else:
                meaning = int(meaning)
                result.append(meaning)
        print(result)


z = Number(5)
z.examination(5)
