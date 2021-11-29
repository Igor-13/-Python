# Реализация структуры "Рейтинг"
numbers = [9, 9, 8, 7, 7, 7, 6, 6, 5, 4, 4, 3, 2, 2, 1]
user_number = float(input('Введите целое число: '))
idx = 0
for num in numbers:
    if user_number <= num:
        idx += 1
    else:
        break

numbers.insert(idx, user_number)
print(numbers)
