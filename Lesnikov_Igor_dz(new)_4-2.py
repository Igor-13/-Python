# Реализация скрипта выводящего значения больше предыдущего

data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [data[n] for n in range(1, len(data)) if data[n] > data[n - 1]]

print(result)
