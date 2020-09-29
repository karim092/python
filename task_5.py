vyrucka = int(input('Введите значение выручки фирмы: '))
izderjki = int(input('Введите значение издержек фирмы: '))

if izderjki > vyrucka:
    print('Предприятие работает в убыток')
else:
    print('Предприятие работает c прибылью')
    prib = vyrucka - izderjki
    rent = prib / vyrucka * 100
    rent = round(rent, 2)
    print(f'Рентабельность выручки: {rent}')
    pers = int(input('Введите численность сотрудников фирмы: '))
    result = prib / pers
    result = round(result, 2)
    print(f'прибыль фирмы в расчете на одного сотрудника: {result}')

