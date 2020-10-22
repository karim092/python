from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, v, name):
        self.v = v
        self._name = name

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    def calculate(self):
        result = (self.v/6.5 + 0.5)
        return round(result, 2)

    @property
    def name(self):
        return self._name

class Suit(Clothes):

    def calculate(self):
        result = (2 * self.v + 0.3)
        return round(result, 2)

    @property
    def name(self):
        return self._name

suit = Suit(150, 'Костюм')
coat = Coat(150, 'Пальто')
print(f'Общий расход ткани на {coat.name} и {suit.name}: {suit.calculate() + coat.calculate()}')





