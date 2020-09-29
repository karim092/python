user_number = input('Введите целое число: ')

i = 0
size = len(user_number)
maximum = []

while i != size:
    maximum.append(user_number[i])
    i += 1

print(max(maximum))

