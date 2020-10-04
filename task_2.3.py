months_list = ['Зима', 'Весна', 'Лето', 'Осень']

user_namber = int(input('Вводите месяц в виде целого числа от 1 до 12: '))

# Решение через list
if user_namber > 0 and user_namber <= 2 or user_namber == 12:
    print(f'Время года - {months_list[0]}')
elif user_namber > 2 and user_namber <= 5:
    print(f'Время года - {months_list[1]}')
elif user_namber > 5 and user_namber <= 8:
    print(f'Время года - {months_list[2]}')
elif user_namber > 8 and user_namber <= 11:
    print(f'Время года - {months_list[3]}')
else:
    print('Ввод не корректный')

# Решение через dict
months_dict = {1: 'месяц: январь, время года - Зима',
               2: 'месяц: февраль, время года - Зима',
               3: 'месяц: март, время года - Весна',
               4: 'месяц: апрель, время года - Весна',
               5: 'месяц: май, время года - Весна',
               6: 'месяц: июнь, время года - Лето',
               7: 'месяц: июль, время года - Лето',
               8: 'месяц: август, время года - Лето',
               9: 'месяц: сентябрь, время года - Осень',
               10: 'месяц: октябрь, время года - Осень',
               11: 'месяц: ноябрь, время года - Осень',
               12: 'месяц: декабрь, время года - Зима'
               }

if user_namber in months_dict:
    print(months_dict.get(user_namber))
else:
    print('Ввод не корректный')
