# файл, где каждая строка описывает учебный предмет
list_of_items = {

}

with open('text_6.txt', 'r', encoding='utf-8') as z:
    for line in z:
        name, stats = line.split(':')
        all_name = sum(map(int, ''.join([x for x in stats if x == ' ' or '9' >= x >= '0']).split()))
        list_of_items[name] = all_name
    print(list_of_items)
