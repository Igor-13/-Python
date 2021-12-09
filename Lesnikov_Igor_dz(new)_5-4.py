# Замена английских числительных русскими

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_4-2.txt', 'w', encoding='utf-8') as z_2:
    with open('text_4.txt', 'r', encoding='utf-8') as z_1:
        z_2.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in z_1])

