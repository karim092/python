class Kletka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = Kletka(self.x + self.y, other.x + other.y)
        return result.x + result.y

    def __sub__(self, other):
        result = Kletka(self.x - self.y, other.x - other.y)
        if result.x - result.y <= 0:
            return 'Меньше нуля'
        else:
            return result.x - result.y

    def __mul__(self, other):
        result = Kletka(self.x + self.y, other.x + other.y)
        return result.x * result.y

    def __floordiv__(self, other):
        result = Kletka(self.x + self.y, other.x + other.y)
        return round(result.x / result.y)

    def make_order(self, kol, l = 0):
        list = []
        el = self.x + self.y
        while l < el:
            l += kol
            if l >= el:
                k = kol - (l - el)
                list.append('*' * k)
                print(''.join(list))
            else:
                list.append('*' * kol + '/n')




x = Kletka(8, 7)
y = Kletka(5, 8)
print(x + y)
print(x - y)
print(x * y)
print(x // y)
x.make_order(5)

