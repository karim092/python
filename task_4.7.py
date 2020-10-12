def fact(x):
    a = 1
    b = 1
    if x == 0:
        a = 1
    elif x < 0:
        print('Введите действительное целое число!')
        quit()
    else:
        while b <= x:
            a = a * b
            b += 1
    yield a

z = int(input('Введите число: '))

for el in fact(z):
    print(el)


