# Реализация функции вывода слов с заглавной буквы


def int_func():
    for text in input("Enter words separated by space: ").split():
        result = 0
        for x in text:
            if 122 >= ord(x) >= 97:
                result += 1
        print(text.title() if result == len(text) else f"Enter words from small english letters {text}")


int_func()
