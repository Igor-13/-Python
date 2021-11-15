# Вычесление результата спортсмена.
result = input('Введите ваш результат пробежки')
goal = input('Введите желаемый результат')
result = int(result)
goal = int(goal)
distance = result
day = 1
while distance < goal:
    progress = (distance * 10) / 100
    distance = distance + progress
    day += 1
print(f'на {day}-й день спортсмен достиг результата — не менее {goal} км')


