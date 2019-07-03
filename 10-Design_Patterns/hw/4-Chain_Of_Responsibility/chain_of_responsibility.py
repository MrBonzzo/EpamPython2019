"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""


class Goods:
    def __init__(self, eggs, flour, milk, sugar, oil, butter):
        self.eggs = eggs
        self.flour = flour
        self.milk = milk
        self.sugar = sugar
        self.oil = oil
        self.butter = butter


class Checker:
    def set_next(self, checker):
        pass

    def check(self, data):
        pass


class BaseChecker(Checker):
    def __init__(self, next=None):
        self.next = next

    def set_next(self, next):
        self.next = next

    def check(self, data):
        if self.next:
            self.next.check(data)


class EggsChecker(BaseChecker):
    def check(self, data):
        if data.eggs >= 2:
            print('eggs: enough')
        else:
            print('eggs: not enough')
        super().check(data)


class FlourChecker(BaseChecker):
    def check(self, data):
        if data.flour >= 300:
            print('flour: enough')
        else:
            print('flour: not enough')
        super().check(data)


class MilkChecker(BaseChecker):
    def check(self, data):
        if data.milk >= 0.5:
            print('milk: enough')
        else:
            print('milk: not enough')
        super().check(data)


class SugarChecker(BaseChecker):
    def check(self, data):
        if data.sugar >= 100:
            print('sugar: enough')
        else:
            print('sugar: not enough')
        super().check(data)


class OilChecker(BaseChecker):
    def check(self, data):
        if data.oil >= 10:
            print('oil: enough')
        else:
            print('oil: not enough')
        super().check(data)


class ButterChecker(BaseChecker):
    def check(self, data):
        if data.butter >= 120:
            print('butter: enough')
        else:
            print('butter: not enough')
        super().check(data)


if __name__ == '__main__':
    checker = EggsChecker()
    flour_checker = FlourChecker()
    milk_checker = MilkChecker()
    sugar_checker = SugarChecker()
    oil_checker = OilChecker()
    butter_checker = ButterChecker()

    checker.set_next(flour_checker)
    flour_checker.set_next(milk_checker)
    milk_checker.set_next(sugar_checker)
    sugar_checker.set_next(oil_checker)
    oil_checker.set_next(butter_checker)

    goods_1 = Goods(eggs=0, flour=0, milk=0, sugar=0, oil=0, butter=0)
    goods_2 = Goods(eggs=1, flour=20, milk=1, sugar=90, oil=20, butter=150)
    goods_3 = Goods(eggs=2, flour=800, milk=2, sugar=900, oil=20, butter=150)

    print('\nGoods_1:')
    checker.check(goods_1)
    print('\nGoods_2:')
    checker.check(goods_2)
    print('\nGoods_3:')
    checker.check(goods_3)
