from sys import argv

script_name, chas, stavka, premya = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", chas)
print("Ставка в час: ", stavka)
print("Премия: ", premya)

chas = int(chas)
stavka = int(stavka)
premya = int(premya)

def zarplata(chas, stavka, premya):
    proc = (chas * stavka) / 100 * premya
    zp =chas * stavka + proc
    print('Расчет заработной платы сотрудника: ', zp)

zarplata(chas, stavka, premya)