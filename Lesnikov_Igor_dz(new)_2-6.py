# Реализация структуры данных "Товары"
my_list = []
products = {'название': '', 'цена': '', 'количество': '', 'еденица измерения': ''}
characteristic = {'название': [], 'цена': [], 'количество': [], 'еденица измерения': []}
idx = 1
while True:
    if input('Для выхода нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    idx += 1
    copy_dict = products.copy()
    for z in products:
        user_answer = input(f'Введите свойство {z} - ')
        copy_dict[z] = int(user_answer) if z == 'количество' else user_answer
        characteristic[z].append(copy_dict[z])
    my_list.append((idx, copy_dict))
    print(f'\nСтруктура товаров\n{my_list}')
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, val in characteristic.items():
        print(f'{key:>30}: {val}')
    print("*" * 30)

