my_list = [7, 5, 3, 3, 2]
print(my_list)

while True:
    user_number = int(input('Введите число: '))
    my_list.append(user_number)
    my_list.sort(reverse=True)
    print(my_list)


