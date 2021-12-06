# Создание файла с записью данных от пользователя


with open('text_1.txt', 'w', encoding='utf-8') as z:
    while True:
        text = input('Введите текст, для записи в файл либо - stop, для остановки: ')
        if text == 'stop':
            break
        print(text, file=z)

