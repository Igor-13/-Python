# Перевод времени
user_name = input('Введите колличество секунд')
user_name = int(user_name)
hour = user_name // 3600
for_minute = user_name % 3600
minute = for_minute // 60
second = for_minute % 60
print(f'Дата {hour:02}:{minute:02}:{second:02}')