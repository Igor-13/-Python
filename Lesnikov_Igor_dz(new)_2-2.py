# Обмен значений
data = list(input(f'Введите целые числа: '))

for num in range(1, len(data), 2):
    data[num - 1], data[num] = data[num], data[num - 1]

print(data)
