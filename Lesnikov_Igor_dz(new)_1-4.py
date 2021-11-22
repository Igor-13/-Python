# Поиск самой большой цифры в числе
number = input('Введите целое число')
number = int(number)
max_number = 0
while number > 0:
    meaning = number % 10
    number = number // 10
    if meaning > max_number:
        max_number = meaning
    else:
        continue

print(max_number)
