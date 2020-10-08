a = float(input('Введите число A: '))
b = float(input('Введите число B: '))
c = float(input('Введите число C: '))

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    le = len(my_list)
    return sum(my_list[le-2:le])

print(my_func(a, b, c))
