# Файл, в котором каждая строка должна содержать данные о фирме.
import json

with open('text_7-2.txt', 'w', encoding='utf-8') as z_1:
    with open('text_7.txt', 'r', encoding='utf-8') as z_2:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in z_2}
        result = [profit, {'average_profit': round(sum([int(n) for n in profit.values() if int(n) > 0]) /
                                                   len([int(n) for n in profit.values() if int(n) > 0]))}]
    json.dump(result, z_1, ensure_ascii=False, indent=4)
