# Работа с переменными
number = 7
color = 'black'
animal = 'dog'
print(number)
print(color)
print(animal)
user_name = input('Введите логин')
user_password = input('Введите пароль')
if user_name == 'admin':
    print('Логин верный!')
else:
    print('Логин не верный! Попробуйте ещё раз!')
if user_password == '123456':
    print('Пароль верный!')
else:
    print('Пароль не верный! Попробуйте ещё раз!')
calculator_1 = input('Введите первое слагаемое для нахождения суммы')
calculator_2 = input('Введите второе слагаемое для нахождения суммы')
calculator_1 = int(calculator_1)
calculator_2 = int(calculator_2)
print(f'сумма чисел равна {calculator_1 + calculator_2}')
