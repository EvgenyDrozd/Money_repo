class Money:
    def __init__(self, rub: int, kop:int):
        self.rub = rub + kop // 100
        self.kop = kop % 100


    def get_rub(self):
        return self.rub

    def get_kop(self):
        return self.kop

    def __add__(self, other):
        return Money(self.rub + other.rub, self.kop + other.kop)

    def __str__(self):
        return f'Monney({self.rub}, {self.kop:02d})'

    def __sub__(self, other):
        """Реализация оператора -"""

    def __truediv__(self, other):
        """Реализация целочисленного деления"""

if __name__ == "__main__":
    money1 = Money(20, 120)
    money2 = Money(30,30)
    print(f'{money1.rub = }, {money1.kop = }')
    print(money1)
    print(money2)
    money3 = money1 + money2
    print(money3)