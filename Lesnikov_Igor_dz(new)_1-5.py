# Вычесление выручки/издержек фирмы.
profit = input('Введите выручку вашего предприятия')
damages = input('Введите издержки вашего предприятия')
profit = int(profit)
damages = int(damages)
if profit > damages:
    difference = profit - damages
    print(f'Ваше предприятие прибыльное! Размер прибыли составляет: {difference}')
    profitability = (difference / profit) * 100
    print(f'Рентабельность вашего предприятия составляет: {profitability:.0f}%')
elif profit < damages:
    print(f'Ваше предприятие работает в убыток! Размер убытков составляет: {damages - profit}')
else:
    print(f'Ваше предприятие откработало в ноль!')
number_of_employees = input('Введите численность сотрудников фирмы')
number_of_employees = int(number_of_employees)
proceeds = profit - damages
employee = proceeds / number_of_employees
if employee > 0:
    print(f'Прибыль фирмы в расчёте на одного сотрудника составляет: {employee:.0f}')
else:
    print(f'Издержки фирмы в расчёте на одного сотрудника составляют: {employee:.0f}')
