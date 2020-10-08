rut = []
def my_func(str):

    if str == 'q':
        quit()

    elif 'q' in str:

        res = str.replace('q','').split(' ')
        if '' in res:
            k = len(res)
            res = res[:k-1]
        rus = list(map(int, res))
        summa = sum(rus)
        rut.append(summa)
        print(sum(rut))
        quit()

    else:

        res = str.split(' ')
        rus = list(map(int, res))
        summa = sum(rus)
        rut.append(summa)
        return sum(rut)


while True:

    user_number = input('Для выхода введите q\nВведите строку чисел, разделенных пробелом: ')
    print(my_func(user_number))
