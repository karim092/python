my_list = []
with open('task_4.txt', 'r', encoding='utf-8') as file:
    for line in file:
        my_list.append(line.strip())
print(my_list)

new_list = []

for el in my_list:
    if 'One' in el:
        new_list.append(el.replace('One', 'Один'))
    if 'Two' in el:
        new_list.append(el.replace('Two', 'Два'))
    if 'Three' in el:
        new_list.append(el.replace('Three', 'Три'))
    if 'Four' in el:
        new_list.append(el.replace('Four', 'Четыре'))
print(new_list)

with open('task_4new.txt', 'w', encoding='utf-8') as file:
        for line in new_list:
            file.write(line + '\n')