while True:
#умножение
    def multiplication(num1, num2):
        return num1 * num2

# деление
    def division(num1, num2):
        return num1 / num2

# сложение
    def plus(num1, num2):
        return num1 + num2

    def minus(num1, num2):
        return num1 - num2

    try:
        num1 = float(input('Введи первое  число:'))
        znak = input('Введи знак операции:')
        num2 = float(input('Введи второе число:'))

        if znak == '*':
            print(multiplication(num1, num2))
        elif znak == '/':
            print(division(num1, num2))
        elif znak == '+':
            print(plus(num1, num2))
        elif znak == '-':
            print(minus(num1, num2))
        else:
            print("Неверный знак операции")
        print('Введи Q выхода')
    except ZeroDivisionError:
        print('Делить на ноль нельзя')

    except ValueError:
        print('Введены некорректные значения')