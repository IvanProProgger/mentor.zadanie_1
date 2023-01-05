class Human:
    default_name = 'Human'
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__house = None
        self.__money = 0
        self.estate = []

    def info(self):
        if self.__house is not None:
            print(f'Имя: {self.name}, возраст: {self.age}, адрес: {", ".join(self.estate)}, сбережения: {self.__money}')
        else:
            print(f'Имя: {self.name}, возраст: {self.age}, адрес: бездомный, сбережения: {self.__money}')

    @classmethod
    def default_info(cls):
        print(cls.default_name, cls.default_age)

    def earn_money(self, amount):
        self.__money += amount

    def __make_deal(self, house, price):
        self.__house = house
        self.__money -= price
        self.estate.append(house)

    def buy_house(self, house, discount):
        if self.__money >= house.final_price(discount):
            self.__make_deal(house.adres, house.final_price(discount))
            print(f'{self.name} купил дом по адресу {house.adres}')
        else:
            print('Денег слишком мало')

class House:

    def __init__(self, area, price, adres):
        self._area = area
        self._price = price
        self.adres = adres #adres для нагладности вывода

    def final_price(self, discount):
        self._price = self._price - self._price * (discount / 100)
        return self._price

h = Human('Andrey', 25)
h.info()
h.earn_money(25)
h.info()
dom1 = House(500, 5000, '5-парковая дом №28')
h.earn_money(5000)
h.buy_house(dom1, 20)
h.info()
dom2 = House(50, 1000, '5-парковая дом №28/4')
h.earn_money(2000)
h.buy_house(dom2, 10)
h.info()

