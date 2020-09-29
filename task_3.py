user_number = int(input('Введите число n: '))
i = 1
new_number = []
new = ''

while i < 4:
    new = f'{new}{user_number}'
    new = int(new)
    new_number.append(new)
    i += 1
'''
user_number_1 = user_number * 11
user_number_2 = user_number * 111

summa = user_number + user_number_1 + user_number_2
'''

print(sum(new_number))