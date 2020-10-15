import json

my_list = []
with open('task_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        my_list.append(line.strip().split())

new_list = []
my_dict = {'firma': '', 'forma':'', 'prib':'','ub':''}
for firma, forma, prib, ubyt in my_list:
    my_dict['firma'] = firma
    my_dict['forma'] = forma
    my_dict['prib'] = prib
    my_dict['prib'] = int(my_dict['prib'])
    my_dict['ub'] = ubyt
    my_dict['ub'] = int(my_dict['ub'])
    new_list.append(my_dict.copy())

print('Прибыль фирм:')

ob_pr = []

for el in new_list:
    print(el['firma'], '-', el['prib'] - el['ub'])
    if el['prib'] - el['ub'] > 0:
        ob_pr.append(int(el['prib']))

sr_prib = sum(ob_pr) / len(ob_pr)

print('Средняя прибыль фирм:')

for el in new_list:
        print(el['firma'], '-', el['prib'] - sr_prib)

one = []
two = []
one_dict = {'firma': '', 'prib': '', 'ub': ''}
two_dict = {'firma': '', 'prib': '', 'ub': ''}

for el in new_list:
    if el['prib'] - el['ub'] > 0:
        one_dict['firma'] = el['firma']
        one_dict['prib'] = el['prib'] - el['ub']
        one_dict['ub'] = '0'
        one.append(one_dict.copy())
    else:
        one_dict['firma'] = el['firma']
        one_dict['ub'] = el['prib'] - el['ub']
        one_dict['prib'] = '0'
        one.append(one_dict.copy())
print(one)
for el in new_list:
    if el['prib'] - sr_prib > 0:
        two_dict['firma'] = el['firma']
        two_dict['prib'] = el['prib'] - sr_prib
        two_dict['ub'] = '0'
        two.append(two_dict.copy())
    else:
        two_dict['firma'] = el['firma']
        two_dict['ub'] = el['prib'] - sr_prib
        two_dict['prib'] = '0'
        two.append(two_dict.copy())
print(two)

with open('task_7new.json', 'w', encoding='utf-8') as f_obj:
        json.dump(one, f_obj)
        f_obj.write('\n')
        json.dump(two, f_obj)



