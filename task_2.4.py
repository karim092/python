user_str = input('Вводие строку из нескольких слов, разделённых пробелами: ')
num = 1

user_str = list(user_str.split(' '))

for el in user_str:
    print(f'{num}. ', el[0:10])
    num += 1