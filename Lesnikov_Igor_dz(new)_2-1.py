# Список различных типов
data = [77, 'abs', [13, 24], (25, -0.5), {7, 96}, 5.6, True, {'a': 'apple', 'o': 'orange'}]

for num, meaning in enumerate(data, 1):
    print(f'{num} - {type(meaning)}')
