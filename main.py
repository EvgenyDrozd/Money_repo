class Money:
    def __init__(self, rub: int, kop:int):
        self.rub = rub + kop // 100
        self.kop = kop % 100


if __name__ == "__main__":
    money1 = Money(20, 120)
    money2 = Money(30,30)
    print(f'{money1.rub = }, {money1.kop = }')