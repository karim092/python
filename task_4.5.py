import random
from functools import reduce

user_len = int(input('Введите длину строки: '))
new_list = []
i = 0
while i != user_len:
    m = random.randrange(100, 1001, 2)
    new_list.append(m)
    i += 1

print(new_list)

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el

print('Сумма всех элементов списка: ', reduce(my_func, new_list))