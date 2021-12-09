# Реализация скрипта в котором предусмотрена функция расчёта заработной платы
from sys import argv


def wage(argv):
    _, output_in_hours, rate_per_hour, prize = argv
    output_in_hours = int(output_in_hours)
    rate_per_hour = int(rate_per_hour)
    prize = int(prize)
    wage_employee = (output_in_hours * rate_per_hour) + prize
    return f' Заработная плата составляет: {wage_employee}'


print(wage(argv))
