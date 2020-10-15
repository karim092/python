#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников
my_list = []
with open('task_3.txt', 'r', encoding='utf-8') as file:
    for line in file:
        my_list.append(line.strip().split())

new_list = []
my_dict = {'Фамилия': '', 'зарплата':''}
for fam, zp  in my_list:
    my_dict['Фамилия'] = fam
    my_dict['зарплата'] = zp
    new_list.append(my_dict.copy())

print('Фамилии сотрудников чей оклад менее 20тыс:')
for el in new_list:
    if int(el['зарплата']) < 20000:
        print(el['Фамилия'])

zarplata = []
for el in new_list:
    zarplata.append(int(el['зарплата']))
print('Средняя величина дохода всех сотрудников:',round((sum(zarplata)/len(zarplata)), 2))
