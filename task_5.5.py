lines = []

while True:
    line = input('Введите числа через пробел\nДля выхода оставьте строку пустым: ')
    lines.append(' ' + line)
    if line == '':
        break

with open('task_5.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line)

new_list = []

with open('task_5.txt', 'r', encoding='utf-8') as file:
    for line in lines:
        k = list(line.split())
        for el in k:
            new_list.append(int(el))
print(new_list)
print(sum(new_list))