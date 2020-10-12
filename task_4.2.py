import random

my_list = []
user_len = int(input('Введите длину строки: '))
def my_func(y):
    i = 0
    while i != y:
        number = random.randint(0, 100)
        my_list.append(number)
        i += 1

my_func(user_len)
print(my_list)

new_list = []
def my_func_new(i):
    k = len(my_list)
    while my_list[i] != my_list[k-1]:
        if my_list[i] < my_list[i+1]:
            new_list.append(my_list[i+1])
        i += 1

my_func_new(0)
print(new_list)







