# Реализация функции суммы чисел


def sum_numbers():
    result = 0
    while True:
        answer = input("Enter numbers separated by a space, to exit press enter 'end': ")
        answer = answer.split(" ")
        for x in answer:
            try:
                if x != 'end':
                    result += int(x)
                else:
                    return f"the sum of the numbers is: {result}"
            except ValueError:
                print("Enter the correct number, or the 'end' to exit")


print(sum_numbers())
