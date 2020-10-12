from itertools import count
from itertools import cycle

nacalo = int(input('Введите начальное число: '))
konec = int(input('Введите конечное число: '))

my_list = []

for el in count(nacalo):
    if el > konec:
        break
    else:
        my_list.append(el)

print(my_list)

kol = int(input('Сколько элементов списка повторить? '))
dlina = len(my_list)

new_list = []
с = 0

for el in cycle(my_list):
    if с > (dlina-1) + kol:
        break
    new_list.append(el)
    с += 1
print(new_list)