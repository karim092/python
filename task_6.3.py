class Worker:
    name = 'Рустам'
    surname = 'Каримов'
    position = 'экономист'
    _income = {"wage": 30000, "bonus": 12000}

class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {Position.surname} {Position.name}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {Position._income["wage"] + Position._income["bonus"]}')

sotrudnik = Position()
sotrudnik.get_full_name()
sotrudnik.get_total_income()