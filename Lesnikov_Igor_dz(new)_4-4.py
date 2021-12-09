# Определение элемента списка, не имеющего повторений

data = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [n for n in data if data.count(n) == 1]

print(result)
