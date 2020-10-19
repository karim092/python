class Stationery:
    title = 'Канцтовары'
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки (ручка).')

class Penсil(Stationery):
    def draw(self):
        print('Запуск отрисовки (карандаш).')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки (маркер).')

a = Stationery()
a.draw()

pen = Pen()
pen.draw()

pencil = Penсil()
pencil.draw()

handle = Handle()
handle.draw()