name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
date = input('Введите дату рождения в формате "ДД.ММ.ГГГГ": ')
city = input('Введите город проживания: ')
email = input('Введите ваш эл. адрес: ')
number = input('Введите номер телефона: ')

def my_func(name=name, surname=surname, date=date, city=city, email=email, number=number):
    print(name, surname, date, city, email, number)

my_func()