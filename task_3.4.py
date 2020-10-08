x = int(input('Введите действительное положительное число x: '))
y = int(input('Введите целое число y: '))

def my_func(x, y):
    step = x ** (-y)
    print(step)

def my_func_2(x, y):
    i = 1
    c = x
    while i != y:
        step = c * x
        c = step
        i += 1
    print(1/step)

my_func(x, y)
my_func_2(x, y)