slova = []
with open('task_2.txt', 'r', encoding='utf-8') as file:
    stroka = 0
    for line in file:
        print(line.strip())
        stroka += 1
        k = line.split()
        sl = len(k)
        slova.append(sl)
print('Количество строк:', stroka,'\nКоличество слов в каждой строке:', slova)



