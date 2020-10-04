user_number = int(input('Введите количество элементов: '))
i = 1
user_list = []

while i <= user_number:
    element = input(f'Введите {i} элемент: ')
    user_list.append(element)
    i += 1

print('Ваш список: ', user_list)

new_list = []
new = []

while len(user_list) >= 2:
    new.append(user_list[0])
    new.append(user_list[1])
    new.reverse()
    new_list.append(new[0])
    new_list.append(new[1])
    user_list.pop(0)
    user_list.pop(0)
else:
    new_list.append(user_list[0])

print('Список с обменом значений соседних элементов: ', new_list)





