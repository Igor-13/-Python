# Вывод фамилий сотрудников получающих меньше 20000.

my_list = {}
with open('text_3.txt', 'r', encoding='utf-8') as z:
    for idx in z:
        my_list[idx.split()[0]]= float(idx.split()[1])
    for key, val in my_list.items():
        if val < 20000:
            print(f'{key} зарабатывает меньше 20000 руб.')
    print(f'Средняя зарплата составляет: {sum(my_list.values()) / len(my_list)}')

