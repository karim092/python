a = float(input('Введите число A: '))
b = float(input('Введите число B: '))

def my_func(a, b):
    try:
        print('Ответ:', round(a / b, 2))
    except ZeroDivisionError:
        print("Деление на 0")

my_func(a, b)
