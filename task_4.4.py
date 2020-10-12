import random

my_list = []
user_len = int(input('Введите длину строки: '))
def my_func(y):
    i = 0
    while i != y:
        number = random.randint(0, 10)
        my_list.append(number)
        i += 1

my_func(user_len)
print(my_list)

new_list = []

for i in my_list:
    k = my_list.count(i)
    if k == 1:
        new_list.append(i)
    i += 1

print(new_list)
