class Road:
    mas_asf_cm = 25
    tol_pol = 5/100
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        itog = lenght * width * Road.mas_asf_cm * Road.tol_pol
        print(f'Расчет массы асфальта: {itog}(т)')

dlina = int(input('Введите длину: '))
shirina = int(input('Введите ширину: '))

a = Road(dlina, shirina)
