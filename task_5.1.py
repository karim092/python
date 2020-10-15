lines = []

while True:
    line = input('Введите строку\nДля выхода оставьте строку пустым: ')
    lines.append(line)
    if line == '':
        break

with open('task_1.txt', 'w', encoding='utf-8') as file:
    for  line in lines:
        file.write(line + '\n')
