tovary_list =[]
tovary = {'Название': '',
          'Цена': '',
          'Количество': '',
          'ед': ''}

i = 0
kolich_tovarov = int(input('Сколько товаров вы хотите внести в список? '))

while i != kolich_tovarov:

    print('Товар №', i+1)
    name = input('Введите название товара: ')
    tovary['Название'] = name
    price = float(input('Введите цену товара: '))
    tovary['Цена'] = price
    quantity = int(input('Введите количество товара: '))
    tovary['Количество'] = quantity
    unit = input('Введите единицу измерения: ')
    tovary['ед'] = unit
    tov = tovary.copy()
    tovary_list.append(tov)
    i+=1

for num in enumerate(tovary_list, 1):
    print(num)

while True:
    analitik = int(input('Какую аналитуку о товарах хотите просмотреть (1: Название 2: Цена 3: Количество 4: ед.изм) введите число: '))
    if analitik == 1:
        nazvanie = []
        for k in tovary_list:
            nazvanie.append(k.get('Название'))
        print('Название: ', nazvanie)
    elif analitik == 2:
        Cena = []
        for k in tovary_list:
            Cena.append(k.get('Цена'))
        print('Цена: ', Cena)
    elif analitik == 3:
        kolich = []
        for k in tovary_list:
            kolich.append(k.get('Количество'))
        print('Количество: ', kolich)
    else:
        ed = []
        for k in tovary_list:
            ed.append(k.get('ед'))
        print('Ед.изм: ', ed)