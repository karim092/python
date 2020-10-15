my_list = []
with open('task_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        my_list.append(line.strip().split())

new_list = []
my_dict = {'предмет': '', 'лекции':'', 'практика':'','лаб':''}
for pr, lek, prak, lab  in my_list:
    my_dict['предмет'] = pr
    my_dict['лекции'] = lek
    my_dict['лекции'] = int(my_dict['лекции'].replace('(л)', '').replace('-', '0'))
    my_dict['практика'] = prak
    my_dict['практика'] = int(my_dict['практика'].replace('(пр)', '').replace('-', '0'))
    my_dict['лаб'] = lab
    my_dict['лаб'] = int(my_dict['лаб'].replace('(лаб)', '').replace('-', '0'))
    new_list.append(my_dict.copy())

for el in new_list:
    print(el['предмет'], sum([el['лекции'], el['практика'], el['лаб']]))
